from playwright.async_api import async_playwright
from playwright_stealth import Stealth
from playwright.async_api import Playwright, Browser, BrowserContext
from config import USER_AGENT, size


async def init_browser() -> tuple[Playwright, Browser]:
    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=True)
    print("Створив браузер і плейрайт")
    return p, browser


async def create_context(p: Playwright, proxy: dict = {}) -> BrowserContext:
    user_agent = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )

    args = [
        f"--user-agent={user_agent}",
        "--window-size=1366,768",
        "--disable-blink-features=AutomationControlled",
    ]

    context = await p.chromium.launch_persistent_context(
        user_data_dir="userdata",
        headless=False,
        locale="uk-UA",
        timezone_id="Europe/Kiev",
        args=args,
    )
    
    # stealth = Stealth()
    # await stealth.apply_stealth_async(context)
    print("Створив контекст")
    return context
