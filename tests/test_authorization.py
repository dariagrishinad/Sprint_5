from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import AUTH
from locators import Locators


class TestStellarBurgerAuthorization:
    def test_authorization_with_button_login_to_account(self, driver):
        email = AUTH.EMAIL
        password = AUTH.PASSWORD
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHECK_BUTTON))

    def test_authorization_with_button_personal_area(self, driver):
        email = AUTH.EMAIL
        password = AUTH.PASSWORD
        driver.find_element(*Locators.PERSONAL_AREA).click()
        driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHECK_BUTTON))

    def test_authorization_with_button_in_registration_form(self, driver):
        email = AUTH.EMAIL
        password = AUTH.PASSWORD
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHECK_BUTTON))

    def test_authorization_with_button_in_password_recovery(self, driver):
        email = AUTH.EMAIL
        password = AUTH.PASSWORD
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.RESTORE_PASSWORD_LINK).click()
        driver.find_element(*Locators.LOGIN_LINK).click()
        driver.find_element(*Locators.EMAIL_FOR_AUTHORIZATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FOR_AUTHORIZATION).send_keys(password)
        driver.find_element(*Locators.AUTH_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHECK_BUTTON))
