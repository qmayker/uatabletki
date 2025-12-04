import re
from patchright.async_api import BrowserContext

async def get_pharmacies_amount(context:BrowserContext, url:str) -> int:
    page = await context.new_page()
    await page.goto(url)

    locator = page.locator(".address-card__top-count.pt-3")
    text = await locator.inner_text()
    amount = list(re.findall(r"\d+", text)) 
    
    return int(amount[0])


async def divide_beetwen_contexts(context_amount:int, context:BrowserContext, url:str):
    pharmacies_amount = await get_pharmacies_amount(context, url)
    divided_tasks = {}
    for i in range(context_amount):
        divided_tasks[str(i)] = []
    counter = 0
    while counter != pharmacies_amount-1:
        for i in range(context_amount):
            divided_tasks[i].append(counter)
            counter += 1 

