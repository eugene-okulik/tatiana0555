import allure
from test_ui_tabramova_pw.pages.base_page import BasePage
from test_ui_tabramova_pw.pages.locators import category_locators as loc
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from playwright.sync_api import expect


class DesksPage(BasePage):
    page_url = '/shop/category/desks-1'

    @allure.step('Check the name "desks" in the selected category')
    def check_name_desks_selected_category_is(self, text: str):
        selected_category = self.page.locator(loc.desks_select_loc)
        expect(selected_category).to_be_visible()
        expect(selected_category).to_have_text(text)
        print(f"Название категории: {selected_category.text_content()}")

    @allure.step('Check sorting price low to high')
    def check_sorted_price_low_to_high(self):
        dropdown_button = self.page.locator(loc.dropdown_button_loc)
        dropdown_button.click()
        expect(self.page.locator(loc.dropdown_menu_loc)).to_be_visible()
        self.page.locator(loc.price_low_to_high_loc).click()
        self.page.wait_for_timeout(1500)  # небольшая пауза на перестроение
        product_elements = self.page.locator(loc.product_elements_loc)
        expect(product_elements.first).to_be_visible()

        # 5. Собираем названия и цены
        count = product_elements.count()
        products = []
        for i in range(count):
            product = product_elements.nth(i)
            try:
                title = product.locator(loc.title_loc).inner_text().strip()
                price_text = product.locator(loc.price_text_loc).inner_text().strip()
                price = float(''.join(filter(lambda x: x.isdigit() or x == '.', price_text)))
                products.append({"title": title, "price": price})
            except Exception as e:
                print(f"Ошибка при обработке товара #{i}: {e}")

        # 6. Выводим список
        print("Список товаров (от меньшей цены к большей):")
        for p in products:
            print(f"{p['title']} — {p['price']}")

        # 7. Проверяем сортировку
        is_sorted = all(products[i]["price"] <= products[i + 1]["price"]
                        for i in range(len(products) - 1))
        print(f"\nПроверка сортировки: {'Успешно' if is_sorted else 'Не успешно'}")
        assert is_sorted, "Товары не отсортированы по возрастанию цены!"

    @allure.step('Check filter by components')
    def check_filter_by_components(self):
        # 1. Список товаров до фильтра
        initial_products = [
            el.inner_text().strip()
            for el in self.page.locator(loc.product_locator_loc).all()
        ]

        print(f"Исходный список товаров ({len(initial_products)} шт.):")
        for name in initial_products:
            print(f"   - {name}")

        # 2. Применяем фильтр "Components"
        components = self.page.locator(loc.components_loc)
        components.click()
        self.page.wait_for_function(
            f"document.querySelectorAll('{loc.new_list_produt_names}').length != {len(initial_products)}"
        )

        # 3. Список после фильтрации
        new_product_names = [
            el.inner_text().strip()
            for el in self.page.locator(loc.new_list_produt_names).all()
        ]

        print('Список товаров после применения фильтра "Components":', new_product_names)

        assert new_product_names != initial_products, "Фильтр 'Components' не сработал: список товаров не изменился!"
        assert len(new_product_names) < len(initial_products), (
            f"Фильтр 'Components' не уменьшил количество товаров: "
            f"было {len(initial_products)}, стало {len(new_product_names)}"
        )

        print(
            f"Фильтр 'Components' успешно применён! "
            f"Количество товаров: было {len(initial_products)}, стало {len(new_product_names)}."
        )

    @allure.step('Check price range')
    def check_price_range(self):
        # 1. Разбор URL
        url = self.page.url
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        # 2. Добавляем фильтр по цене
        params['min_price'] = ['300']
        params['max_price'] = ['2000']

        # 3. Новый URL
        new_query = urlencode(params, doseq=True)
        new_url = urlunparse(parsed._replace(query=new_query))

        # 4. Переходим на новый URL
        self.page.goto(new_url)
        self.page.wait_for_load_state('networkidle')

        # 5. Проверяем товары
        min_price, max_price = 300, 2000
        invalid_products = []
        product_cards = self.page.locator(loc.products_loc)

        for i in range(product_cards.count()):
            card = product_cards.nth(i)
            try:
                name = card.locator(loc.name_loc).inner_text().strip()
                price_text = card.locator(loc.price_text_loc).inner_text().replace(",", "").strip()
                price = float(''.join(filter(lambda x: x.isdigit() or x == '.', price_text)))
                print(f"{name}: {price} $")

                if not (min_price <= price <= max_price):
                    invalid_products.append((name, price))

            except Exception as e:
                print("Ошибка при обработке карточки:", e)

        # 6. Проверка результатов
        if invalid_products:
            for name, price in invalid_products:
                print(f"Товар '{name}' не соответствует диапазону цен: {price} $")

            expect(
                len(invalid_products) == 0,
                f"Найдены товары вне диапазона {min_price}-{max_price} $"
            ).to_be_truthy()
        else:
            print(f"Все товары соответствуют диапазону цен {min_price}-{max_price} $.")
