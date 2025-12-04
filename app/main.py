import asyncio
import random
from patchright.async_api import async_playwright
from app.scraper.browser import create_context
from app.scraper.scraper import scrape
from app.scraper.thread_managment import divide_beetwen_contexts
from config import proxies


async def start():
    URL = "https://tabletki.ua/uk/pharmacy/%D0%9F%D0%B0%D0%B2%D0%BB%D0%BE%D0%B3%D1%80%D0%B0%D0%B4/"
    async with async_playwright() as p:
        context = await create_context(p, random.choice(proxies))
        # contexts = []
        # for proxy in proxies:
        #     context = await create_context(p=p, proxy=proxy)
        #     contexts.append(context)
        # divided_tasks = await divide_beetwen_contexts(
        #     len(contexts), random.choice(contexts), URL
        # )
        # print(divided_tasks)
        # await get_pharmacies_amount(context, URL)
        print("Створив контекст")
        r = await scrape(
            context,
            URL,
        )
        if not r.success:
            r = await scrape(
                context, 
                URL, 
                r.counter,
                r.pharmacies
            )
        print("Завершив скрапінг")


if __name__ == "__main__":
    asyncio.run(start())
