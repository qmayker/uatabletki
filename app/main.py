import asyncio
from app.scraper.browser import init_browser, create_context
from app.scraper.scraper import scrape


async def start():
    p, browser = await init_browser()
    context = await create_context(p=p)
    print("Створив контекст")
    r = await scrape(context, "https://tabletki.ua/uk/pharmacy/kiev/")  # noqa: F841
    print("Завершив скрапінг")
    await context.close()
    await p.stop()


if __name__ == "__main__":
    asyncio.run(start())
