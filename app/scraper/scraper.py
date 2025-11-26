from playwright.async_api import BrowserContext


async def scrape(context: BrowserContext, url: str):
    page = await context.new_page()
    r = await page.goto(url=url)
    print(r.status)  # type: ignore
    await page.mouse.wheel(0, 500)
