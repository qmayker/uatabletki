import asyncio
from patchright.async_api import BrowserContext
from patchright.async_api import Page, Locator
from app.scraper.types import Item, Pharmacy, TaskResult


async def scrape_category_menu(page: Page) -> list[Item]:
    # print("Відкрив конкретну категорію")
    items_list = []
    await page.wait_for_selector(".category-holder")
    category = page.locator(".category-holder")
    items = category.locator(".quantity__info--count")

    for i in range(await items.count()):
        item = items.nth(i)
        item_name = await item.locator("h2").text_content()
        item_price = await item.locator(
            ".quantity__info--amount.mb-3.strong"
        ).inner_text()
        items_list.append(Item(name=item_name, price=item_price))  # type: ignore
    await back_to_cat_menu(page)

    return items_list


async def open_categories_menu(page: Page) -> list[list[Item]]:
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


async def show_more_results(page: Page) -> list[Locator]:
    show_button = page.get_by_text("Показати ще")
    await show_button.click()
    pharmacies = await page.locator(".address-card").all()

    return pharmacies


async def get_to_current_page(counter: int, page: Page) -> list[Locator]:
    pharmacies = await page.locator("article.address-card").all()
    if counter == 0:
        return pharmacies
    while len(pharmacies) - 2 < counter:
        await show_more_results(page)
        pharmacies = await page.locator("article.address-card").all()
    return pharmacies


async def scrape(
    context: BrowserContext, url: str, counter: int = 0, pharmacies_list: list = list()
) -> TaskResult:
    page = await context.new_page()
    await page.goto(url)
    try:
        pharmacies = await get_to_current_page(counter, page)
    except Exception:
        return TaskResult(success=False, pharmacies=pharmacies_list, counter=counter)
    while True:
        try:
            await asyncio.sleep(0.01)
            current_pharmacy = pharmacies[counter]
            print(current_pharmacy)
            name = (
                await current_pharmacy.locator(
                    ".address-card__header--name.icon-holder"
                ).all_text_contents()
            )[0]
            print(name.strip())

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
            if counter == len(pharmacies) - 1:
                print("Відкриваю нові аптеки")
                pharmacies = await show_more_results(page)
        except Exception:
            return TaskResult(
                success=False, pharmacies=pharmacies_list, counter=counter
            )
