import asyncio
from playwright.async_api import BrowserContext


async def scrape(context: BrowserContext, url: str):
    page = await context.new_page()
    r = await page.goto(url=url)
    print(r.status)  # type: ignore
    r = await page.evaluate("window.scrollBy(0, window.innerHeight);")
    await asyncio.sleep(3)
