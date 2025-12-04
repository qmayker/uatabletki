import random
import asyncio
import nodriver as uc
from config import proxies
# python -m app.scraper.no_driver.browser


async def start_browser(proxy: dict):
    URL = "https://tabletki.ua/uk/pharmacy/%D0%9F%D0%B0%D0%B2%D0%BB%D0%BE%D0%B3%D1%80%D0%B0%D0%B4/"
    browser = await uc.start(
        browser_executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
        no_sandbox=True,  # type: ignore
        debugger_port=9222,  # type: ignore
        # proxy=proxy
    )
    page = await browser.get(URL)
    await asyncio.sleep(1)
    elms = await page.select_all("article.address-card")
    # for elm in elms:
    elm = elms[0]
    input = await elm.query_selector('[placeholder="Шукати товари тут"]')
    await input.click()  # type: ignore
    categories = await page.select_all(".tag.ui-menu-item-wrapper")
    print(categories)
    for category in categories:
        await category.click()
        await asyncio.sleep(0.1)
        back_button = await page.select(".back-search.mr-3")
        await asyncio.sleep(0.1)
        await back_button.click()
    close_button = (await page.select_all(".modal-content-wrapper .modal-header .close"))[0]
    print("\n", close_button)
    await close_button.click()
    await asyncio.sleep(60)


if __name__ == "__main__":
    uc.loop().run_until_complete(start_browser(random.choice(proxies)))
