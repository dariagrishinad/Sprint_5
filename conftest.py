import pytest
from selenium import webdriver

from constants import AUTH, URLS
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(URLS.MAIN_URL)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
    driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(AUTH.EMAIL)
    driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(AUTH.PASSWORD)
    driver.find_element(*Locators.AUTH_BUTTON).click()
    return driver
