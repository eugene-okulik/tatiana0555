from test_ui_tabramova_pw.pages.base_page import BasePage
import allure
from test_ui_tabramova_pw.pages.locators import product_locators as loc
from playwright.sync_api import expect


class ProductPage(BasePage):
    page_url = '/shop/furn-9999-office-design-software-7?category=9'

    @allure.step('Check page Terms and conditions')
    def check_page_terms_and_conditions(self, text: str):
        # Кликаем по ссылке "Terms and Conditions"
        self.page.locator(loc.terms_link_loc).click()
        self.page.wait_for_url("**/terms")

        # Проверяем, что текст соответствует ожидаемому
        standard_terms = self.page.locator(loc.standard_terms_loc)
        expect(standard_terms).to_be_visible()
        expect(standard_terms).to_have_text(text)
        print(f"Заголовок секции: {standard_terms.text_content()}")
        self.page.go_back()

    @allure.step('Check price of product by quantify')
    def check_price_of_product_by_quantity(self, message: str):
        # 1. Считываем цену за одну единицу товара
        price_element = self.page.locator(loc.price_text_loc).first
        expect(price_element).to_be_visible()
        price_text = price_element.inner_text().strip().replace(',', '')
        unit_price = float(price_text)
        print(f"Цена за одну единицу товара: {unit_price}")

        # 2. Увеличиваем количество на 4 клика
        plus_button = self.page.locator(loc.plus_button_loc)
        for _ in range(4):
            plus_button.click()

        # 3. Добавляем товар в корзину
        self.page.locator(loc.add_cart_button_loc).click()

        # 4. Ждём появления уведомления
        self.page.locator(loc.alert_loc).wait_for(state="visible")
        # expect(self.page.locator(loc.alert)).to_be_visible()

        # 5. Переходим в корзину
        self.page.locator(loc.view_cart_loc).click()

        # 6. Сохраняем старую сумму
        old_cart_price = self.page.locator(loc.cart_price_text_loc).inner_text().strip()

        # 7. Уменьшаем кол-во товара на 1 и ожидаем изменение суммы
        self.page.locator(loc.minus_in_cart_loc).click()
        cart_price_el = self.page.locator(loc.cart_price_text_loc)
        expect(cart_price_el).not_to_have_text(old_cart_price)

        # 8. Проверяем итоговую сумму
        quantity_value = int(self.page.locator(loc.quantity_input_loc).get_attribute("value"))
        cart_total = float(self.page.locator(loc.cart_price_text_loc).inner_text().strip().replace(',', ''))
        expected_total = round(unit_price * quantity_value, 2)
        print(f"Ожидали: {expected_total}, получили: {cart_total}")

        assert cart_total == expected_total, f"Ошибка: ожидали {expected_total}, а получили {cart_total}"
        print(message)

    @allure.step('Check invalid promo code')
    def check_invalid_promo_code(self, message: str):
        # Добавляем товар в корзину
        self.page.locator(loc.add_cart_button_loc).click()
        self.page.locator(loc.alert_loc).wait_for(state="visible")
        self.page.locator(loc.view_cart_loc).click()

        # Вводим промокод
        self.page.locator(loc.input_promo_loc).fill("test")
        self.page.locator(loc.button_apply_loc).click()

        # Проверяем наличие предупреждения
        alert = self.page.locator(loc.alert_element_loc)
        if alert.is_visible():
            print("Появилось предупреждение:", message)
        else:
            print("Предупреждение не появилось.")

    @allure.step('Check required fields are empty')
    def check_required_fields_are_empty(self, message: str):
        # Проверка выбора валюты, если доступен
        if self.page.locator(loc.select_currency_loc).is_visible():
            self.page.locator(loc.select_currency_loc).click()
            self.page.locator(loc.eur_option_loc).click()
            price_block = self.page.locator(loc.price_block_loc)
            expect(price_block).to_be_visible()
            price_text = price_block.inner_text().strip()
            print("Текст цены:", price_text)
            assert "€" in price_text, f"Ожидали символ €, но получили: {price_text}"
            print("Цена отображается в евро:", price_text)
        else:
            print("Кнопка выбора валюты не найдена, добавляем товар в корзину.")

        # Добавляем товар в корзину
        self.page.locator(loc.add_cart_button_loc).click()
        self.page.locator(loc.alert_loc).wait_for(state="visible")
        self.page.locator(loc.view_cart_loc).click()

        # Переход к оформлению
        self.page.locator(loc.button_checkout_loc).click()
        self.page.wait_for_url("**/address")
        self.page.locator(loc.button_continue_checkout_loc).click()

        note = self.page.locator(loc.note_empty_fields_loc).first
        expect(note).to_be_visible()
        expect(note).to_contain_text(message)

        print("Появилось предупреждение:", message)
