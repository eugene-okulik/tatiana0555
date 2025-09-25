from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_first(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 10)

    #  откройте первый (Customizable Desk) товар в новой вкладке
    link = driver.find_element(By.LINK_TEXT, 'Customizable Desk')
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

    #  Перейдите на вкладку с товаром
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Добавьте товар в корзину:
    # - Нажмите на кнопку Add to Cart
    driver.find_element(By.ID, 'add_to_cart').click()

    # - В открывшемся попапе нажмите Continue shopping
    button_shopping = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'btn-secondary'))
    )
    button_shopping.click()

    # Закройте вкладку с товаром
    driver.close()

    # Переключитесь обратно на основную вкладку
    driver.switch_to.window(tabs[0])
    driver.refresh()

    # Откройте корзину
    # Убедитесь, что в корзине тот товар, который вы добавляли
    # result = driver.find_element(By.ID, 'cart_products')
    # assert result.text == 'Customizable Desk (Steel, White)\n160x80cm, with large legs.\nRemove\n$ 750.00'

    driver.find_element(By.CSS_SELECTOR, 'i.fa.fa-shopping-cart.fa-stack').click()
    assert 'Customizable Desk' in driver.find_element(By.TAG_NAME, 'h6').text

    #
    # # Закройте вкладку с товаром
    # driver.close()
    # driver.switch_to.window(tabs[0])
    # driver.refresh()
    # driver.find_element(By.CLASS_NAME, 'fa-shopping-cart').click()
    # 'fa fa-shopping-cart fa-stack'
    #
    # # 8. Убедитесь, что в корзине тот товар, который вы добавляли
    # result = driver.find_element(By.TAG_NAME, 'h6')
    # # assert result.text == 'Customizable Desk (Steel, White)'
    # assert 'Customizable Desk' in result.text
    #
    # # assert result.text == 'Customizable Desk (Steel, White)\n160x80cm, with large legs.\nRemove\n$ 750.00'


def test_second(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 10)

    # навести мышку на первый товар (на картинку товара)
    # нажать появившуюся кнопку корзины
    actions = ActionChains(driver)
    picture = driver.find_element(By.CSS_SELECTOR, 'a.oe_product_image_link span img')
    cart = driver.find_element(By.CSS_SELECTOR, 'span.fa.fa-shopping-cart')
    actions.move_to_element(picture).click(cart).perform()

    # в появившемся попапе проверить, что товар, на котором нажимали кнопку корзины, появился в этом попапе
    result = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-name.product_display_name'))
    )
    assert result.text == '[FURN_0096] Customizable Desk (Steel, White)'


def test_card(driver):
    wait = WebDriverWait(driver, 10)
    driver.get('http://testshop.qa-practice.com/')
    cards = driver.find_elements(By.CSS_SELECTOR, '[class="oe_product_image_link '
                                                  'd-block h-100 position-relative"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(cards[0]).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    driver.find_element(By.ID, 'add_to_cart').click()
    btn_continue = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn.btn-secondary')))
    btn_continue.click()
    driver.close()
    driver.switch_to.window(tabs[0])
    driver.refresh()
    driver.find_element(By.CSS_SELECTOR, 'i.fa.fa-shopping-cart.fa-stack').click()
    assert 'Customizable Desk' in driver.find_element(By.TAG_NAME, 'h6').text
