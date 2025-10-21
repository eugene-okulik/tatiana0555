from test_ui_tabramova_pw.pages.base_page import BasePage
from playwright.sync_api import expect
import allure
from test_ui_tabramova_pw.pages.locators import cart_locators as loc


class CartPage(BasePage):
    page_url = '/shop/cart'

    @allure.step('Check page section title')
    def check_page_section_title_is(self, text: str):
        order_overview = self.page.locator(loc.order_overview_loc)
        expect(order_overview).to_be_visible()
        actual_text = order_overview.text_content().strip()
        print(actual_text)
        assert actual_text == text, f"Ожидали '{text}', а получили '{actual_text}'"

    @allure.step('Check message in the section')
    def check_message_in_the_section(self, text: str):
        empty_message = self.page.locator(loc.cart_empty_loc)
        expect(empty_message).to_be_visible(timeout=10000)  # Увеличен таймаут до 10 секунд
        # expect(empty_message).to_be_visible()
        actual_text = empty_message.text_content().strip()
        print(actual_text)
        assert actual_text == text, f"Ожидали '{text}', а получили '{actual_text}'"

    @allure.step('Check click on the logo ')
    def check_transition_to_logo(self):
        your_logo = self.page.locator(loc.click_your_loc).first
        expect(your_logo).to_be_visible()
        your_logo.click()
        # Ждём перехода на нужный URL
        expected_url = "http://testshop.qa-practice.com/"
        self.page.wait_for_url(expected_url)
        # Проверяем текущий URL
        current_url = self.page.url
        print(f"Текущий URL: {current_url}")
        assert current_url == expected_url, (
            f"Ожидали переход на {expected_url}, а оказались на {current_url}"
        )
