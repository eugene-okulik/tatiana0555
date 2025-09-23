"""
Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2,
нажмет Start, и проверит, что на странице появляется текст "Hello World!"
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait


def test_dropdown(driver, wait):
    option_text = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    dropdown = driver.find_element(By.ID, 'id_choose_language')
    dropdown_select = Select(dropdown)
    dropdown_select.select_by_visible_text(option_text)
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'result-text')))
    result_text = driver.find_element(By.ID, 'result-text')
    assert option_text == result_text.text, 'Wrong text'


def test_loader(driver, wait):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    button = driver.find_element(By.CSS_SELECTOR, '#start > button')
    button.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'finish')))
    text = driver.find_element(By.ID, 'finish')
    assert text.is_displayed()
