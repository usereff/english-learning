
import pytest
from playwright.sync_api import sync_playwright

from utilities.config import BASE_URL
from pages.home_page import HomePage


@pytest.fixture(scope="session")
def site_page():

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False
        )

        context = browser.new_context()
        page = context.new_page()

        page.goto(BASE_URL)

        yield page

        context.close()
        browser.close()


@pytest.fixture(scope="session")
def home_page(site_page):

    return HomePage(site_page)
