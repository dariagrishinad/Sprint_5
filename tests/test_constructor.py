from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


class TestStellarBurgerConstructor:
    def test_constructor_sauces(self, driver):
        driver.find_element(*Locators.CONSTRUCTOR_SAUCES).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.COLLECT_BURGER))

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.CONSTRUCTOR_SAUCES).get_attribute("class")

    def test_constructor_fillings(self, driver):
        driver.find_element(*Locators.CONSTRUCTOR_FILLINGS).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.COLLECT_BURGER))

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.CONSTRUCTOR_FILLINGS).get_attribute("class")

    def test_constructor_buns(self, driver):
        driver.find_element(*Locators.CONSTRUCTOR_SAUCES).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUNS).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.COLLECT_BURGER))

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(*Locators.CONSTRUCTOR_BUNS).get_attribute("class")
