from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Auth
from locators import Locators

faker = Faker()


class TestStellarBurgerRegistration:
    def test_successful_registration(self, driver):
        name = Auth.NAME
        email = faker.email()
        password = Auth.PASSWORD
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_FOR_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_REGISTRATION).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_TEXT))

    def test_registration_with_invalid_password(self, driver):
        name = Auth.NAME
        email = faker.email()
        password = '12345'
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_FOR_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_REGISTRATION).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INVALID_PASSWORD))
