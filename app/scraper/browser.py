from fake_useragent import UserAgent
from playwright.async_api import async_playwright
from playwright.async_api import Playwright, Browser, BrowserContext
from app.scraper.utils.get_size import get_size


async def init_browser() -> tuple[Playwright, Browser]:
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False)
    return p, browser


async def create_context(browser: Browser, proxy: dict = {}) -> BrowserContext:
    ua = UserAgent()
    client = ua.getChrome
    print(client)
    get_size(client["os"]) # type: ignore
    context = await browser.new_context(
        user_agent=client["useragent"],

        locale="uk-UA",
        timezone_id="Europe/Kiev",
        color_scheme="light",
        record_video_dir="videos/"
    )  
    return context


