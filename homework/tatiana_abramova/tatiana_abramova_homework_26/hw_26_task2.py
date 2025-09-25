from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


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
