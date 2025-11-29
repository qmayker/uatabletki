import asyncio
from playwright.async_api import async_playwright
from app.scraper.browser import init_browser, create_context
from app.scraper.scraper import scrape


async def start():
    async with async_playwright() as p:
        context = await create_context(p=p)
        print("Створив контекст")
        await scrape(
            context,
            "https://tabletki.ua/uk/pharmacy/%D0%9F%D0%B0%D0%B2%D0%BB%D0%BE%D0%B3%D1%80%D0%B0%D0%B4/",
        )
        print("Завершив скрапінг")


if __name__ == "__main__":
    asyncio.run(start())
