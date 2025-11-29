
from playwright_stealth import Stealth
from playwright.async_api import Playwright, Browser, BrowserContext
from config import args


async def init_browser(p:Playwright) -> Browser:
    browser = await p.chromium.launch(headless=True)
    print("Створив браузер")
    return browser


async def create_context(p: Playwright, proxy: dict = {}) -> BrowserContext:
    context = await p.chromium.launch_persistent_context(
        user_data_dir="userdata",
        headless=False,
        locale="uk-UA",
        timezone_id="Europe/Kiev",
        args=args,
    )

    stealth = Stealth()
    await stealth.apply_stealth_async(context)
    print("Створив контекст")
    return context
