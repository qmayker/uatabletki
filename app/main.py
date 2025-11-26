import asyncio
from app.scraper.browser import init_browser, create_context
from app.scraper.scraper import scrape

async def start():
    p, browser = await init_browser()
    context = await create_context(browser=browser)
    r  = await scrape(context, "https://en.wikipedia.org/wiki/Web_scraping")
    await context.close()
    await p.stop()

if __name__ == "__main__":
    asyncio.run(start())