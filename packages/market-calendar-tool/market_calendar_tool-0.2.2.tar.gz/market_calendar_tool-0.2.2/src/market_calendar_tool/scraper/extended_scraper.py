import asyncio
import json
from concurrent.futures import ThreadPoolExecutor

import aiohttp
from loguru import logger

from market_calendar_tool.scraper.models import ScrapeOptions, ScrapeResult

from .base_scraper import BaseScraper
from .data_processor import DataProcessor


class ExtendedScraper:
    def __init__(self, base_scraper: BaseScraper, options: ScrapeOptions):
        self.base_scraper = base_scraper
        self.options = options

    def __getattr__(self, name):
        return getattr(self.base_scraper, name)

    def scrape(self) -> ScrapeResult:
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return asyncio.run(self._async_scrape())
        else:
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(self._run_coroutine, self._async_scrape())
                return future.result()

    async def _async_scrape(self) -> ScrapeResult:
        base_result = self.base_scraper.scrape()
        df_base = base_result.base
        event_ids = df_base["id"].tolist()
        semaphore = asyncio.Semaphore(self.options.max_parallel_tasks)

        async with aiohttp.ClientSession() as session:
            tasks = [
                self._bounded_fetch_event_details(semaphore, session, event_id)
                for event_id in event_ids
            ]
            scrape_results = await asyncio.gather(*tasks, return_exceptions=True)

            successful_results = []
            for event_id, result in zip(event_ids, scrape_results):
                if isinstance(result, Exception):
                    logger.error(f"Error fetching event_id {event_id}: {result}")
                    continue
                else:
                    successful_results.append(result)

            processor = DataProcessor(successful_results)

            base_result.specs = processor.to_specs_df()
            base_result.history = processor.to_history_df()
            base_result.news = processor.to_news_df()

            return base_result

    def _run_coroutine(self, coroutine) -> ScrapeResult:
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        try:
            result = new_loop.run_until_complete(coroutine)
            return result
        finally:
            new_loop.close()

    async def _bounded_fetch_event_details(
        self,
        semaphore: asyncio.Semaphore,
        session: aiohttp.ClientSession,
        event_id: int,
    ):
        async with semaphore:
            return await self._fetch_event_details(session, event_id)

    async def _fetch_event_details(self, session: aiohttp.ClientSession, event_id: int):
        url = f"{self.base_url}/details/{self.site_number}-{event_id}"
        try:
            async with session.get(url, headers=self.session.headers) as response:
                response.raise_for_status()
                try:
                    data = await response.json()
                except json.JSONDecodeError as e:
                    logger.error(f"JSON decode error for event_id {event_id}: {e}")
                    raise
        except aiohttp.ClientError as e:
            logger.error(f"Client error for event_id {event_id}: {e}")
            raise
        except asyncio.TimeoutError as e:
            logger.error(f"Timeout error for event_id {event_id}: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error for event_id {event_id}: {e}")
            raise

        return data
