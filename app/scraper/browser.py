import random
from patchright.async_api import Playwright, BrowserContext


async def create_context(p: Playwright, proxy: dict) -> BrowserContext:
    context = await p.chromium.launch_persistent_context(
        user_data_dir="/tmp/patchright_profile",  # Use a real profile
        channel="chrome",  # Use real Chrome, not Chromium
        headless=False,  # Never use headless for critical scraping
        no_viewport=True,  # Disable viewport to use native resolution
        proxy=proxy, # type: ignore
    )

    print("Створив контекст")
    return context
