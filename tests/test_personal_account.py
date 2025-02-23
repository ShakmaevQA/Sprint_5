import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators

class TestPersonalAccount:
    def test_go_to_personal_account(self, driver, email, password):

        driver.find_element(*Locators.login_button_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.login_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_logout_from_personal_account(self, driver_login, email, password):

        driver_login.find_element(*Locators.field_email_login).send_keys(email)
        driver_login.find_element(*Locators.field_password_login).send_keys(password)
        driver_login.find_element(*Locators.login_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        driver_login.find_element(*Locators.account_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.save_button))

        driver_login.find_element(*Locators.logout_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.login_button))


        assert driver_login.current_url == 'https://stellarburgers.nomoreparties.site/login'