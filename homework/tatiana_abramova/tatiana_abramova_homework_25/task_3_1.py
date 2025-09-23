"""
Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/select/single_select,
выбирает какой-нибудь вариант из Choose language, кликает Submit и проверяет,
что в окошке с результатом отображается тот вариант, который был выбран.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    return chrome_driver


def test_choose_language(driver):
    wait = WebDriverWait(driver, 10)
    data_text = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    dropdown = driver.find_element(By.ID, 'id_choose_language')
    dropdown_select = Select(dropdown)
    dropdown_select.select_by_visible_text(data_text)
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    wait.until(EC.visibility_of_element_located((By.ID, 'result-text')))
    result_text = driver.find_element(By.ID, 'result-text')
    assert data_text == result_text.text
