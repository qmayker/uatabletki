from fake_useragent import UserAgent
from playwright.async_api import async_playwright
from playwright.async_api import Playwright, Browser, BrowserContext


async def init_browser() -> tuple[Playwright, Browser]:
    p = await async_playwright().start()
    browser = await p.chromium.launch()
    return p, browser


async def create_context(browser: Browser, proxy: dict = {}) -> BrowserContext:
    ua = UserAgent()
    print(ua)
    context = await browser.new_context(
        locale="uk-UA",
        timezone_id="Europe/Kiev",
        color_scheme="light",
        viewport={"width": 1920, "height": 1080},
        record_video_dir="videos/"
    )  
    return context


