from playwright.sync_api import Page, Locator
import allure


class BasePage:
    base_url = 'http://testshop.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    @allure.step('Open the page')
    def open_page(self):
        if self.page_url:
            # гарантируем, что URL склеится правильно
            if not self.page_url.startswith("/"):
                self.page_url = "/" + self.page_url
            self.page.goto(f"{self.base_url}{self.page_url}")
        else:
            raise NotImplementedError("Page can not be opened for this page class")

    @allure.step('Find element by locator')
    def find(self, locator) -> Locator:
        return self.page.locator(locator)
