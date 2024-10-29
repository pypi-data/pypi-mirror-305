from datetime import datetime, timedelta
from typing import Optional

from loguru import logger

from market_calendar_tool.scraper.models import ScrapeOptions, Site

from .cleaning.cleaner import clean_data
from .scraper import BaseScraper, ExtendedScraper, ScrapeResult


def scrape_calendar(
    site: Site = Site.FOREXFACTORY,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    extended: bool = False,
    options: Optional[ScrapeOptions] = None,
) -> ScrapeResult:
    def validate_and_format_date(date_str, default_date):
        if date_str:
            try:
                return datetime.strptime(date_str, "%Y-%m-%d")
            except ValueError:
                raise ValueError(f"Date {date_str} is not in the format YYYY-MM-DD")
        return default_date

    today = datetime.now()
    date_from_dt: datetime = validate_and_format_date(date_from, today)
    date_to_dt: datetime = validate_and_format_date(
        date_to, (today + timedelta(days=7))
    )

    if date_to_dt < date_from_dt:
        raise ValueError(
            f"End date (date_to: {date_to_dt.strftime('%Y-%m-%d')}) "
            f"cannot be earlier than start date (date_from: {date_from_dt.strftime('%Y-%m-%d')})."
        )

    date_from_str: str = date_from_dt.strftime("%Y-%m-%d")
    date_to_str: str = date_to_dt.strftime("%Y-%m-%d")

    logger.info(f"Scraping calendar from {date_from_str} to {date_to_str}")

    base_scraper = BaseScraper(site, date_from_str, date_to_str)
    if extended:
        if options is None:
            options = ScrapeOptions()
        return ExtendedScraper(base_scraper, options=options).scrape()
    else:
        return base_scraper.scrape()


def clean_calendar_data(scrape_result: ScrapeResult) -> ScrapeResult:
    cleaned_result = clean_data(scrape_result)

    return cleaned_result
