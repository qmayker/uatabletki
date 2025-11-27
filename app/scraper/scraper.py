import asyncio
from random import randint
from playwright.async_api import BrowserContext


async def scrape(context: BrowserContext, url: str):
    page = await context.new_page()
    r = await page.goto(url=url)
    print(r.status)  # type: ignore
    
    while True:
        # await page.mouse.wheel(0, randint(75, 250))
        locator = page.locator("#showMoreResults")
        # print(await locator.is_visible())
        await asyncio.sleep(0.1)

