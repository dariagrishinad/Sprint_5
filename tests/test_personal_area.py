from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestStellarBurgerPersonalArea:
    def test_transition_to_personal_area(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_AREA).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.CHANGE_PERSONAL_INFORMATION))

    def test_transition_to_constructor(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_AREA).click()
        driver.find_element(*Locators.CONSTRUCTOR_LINK).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.COLLECT_BURGER))

    def test_transition_to_logo(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_AREA).click()
        driver.find_element(*Locators.LOGO_LINK).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.COLLECT_BURGER))

    def test_logout(self, login):
        driver = login
        driver.find_element(*Locators.PERSONAL_AREA).click()
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.LOGIN_TEXT))
