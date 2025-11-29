import asyncio
from random import randint
from playwright.async_api import BrowserContext
from playwright.async_api import Page
from app.scraper.types import Item, Pharmacy


async def scrape_category_menu(page: Page) -> list[Item]:
    print("Відкрив конкретну категорію")
    items_list = []
    await page.wait_for_selector(".category-holder")
    category = page.locator(".category-holder")
    items = category.locator(".quantity__info--count")

    for i in range(await items.count()):
        item = items.nth(i)
        item_name = await item.locator("h2").text_content()
        item_price = await item.locator(".quantity__info--amount").text_content()
        items_list.append(Item(name=item_name, price=item_price))  # type: ignore
    await back_to_cat_menu(page)

    return items_list


async def open_categories_menu(page: Page) -> list[list[Item]]:
    print("Відкриваю меню з категоріями")
    await page.wait_for_selector(".tag-holder.ui-menu-item")
    categories = page.locator(".tag-holder.ui-menu-item")
    cat_list = []
    buttons = categories.locator("button")
    for i in range(await buttons.count()):
        await buttons.nth(i).click()
        items = await scrape_category_menu(page)
        cat_list.append(items)
    await close_menu(page)
    return cat_list


async def close_menu(page: Page):
    close_button = page.get_by_role("button", name="close")
    await close_button.click()


async def back_to_cat_menu(page: Page):
    back_button = page.locator(".back-search")
    await back_button.click()


async def scrape(context: BrowserContext, url: str):
    pharmacies_list = []
    page = await context.new_page()
    await page.goto(url=url)
    counter = 0
    while True:
        pharmacies = page.locator(".address-card")
        await asyncio.sleep(0.05)
        current_pharmacy = pharmacies.nth(counter)
        name = await current_pharmacy.locator(
            ".address-card__header--name"
        ).text_content()
        input = current_pharmacy.get_by_placeholder("Шукати товари тут")
        await input.click()
        items = await open_categories_menu(page)

        pharmacies_list.append(
            Pharmacy(
                name=name.strip(),  # type: ignore
                items=items,
            )
        )
        counter += 1
