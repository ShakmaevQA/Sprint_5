import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators


class TestConstructor:
    def test_go_to_constructor_from_personal_account(self, driver_login, email, password):

        driver_login.find_element(*Locators.field_email_login).send_keys(email)
        driver_login.find_element(*Locators.field_password_login).send_keys(password)
        driver_login.find_element(*Locators.login_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        driver_login.find_element(*Locators.constructor_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))


        assert driver_login.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_go_to_constructor_by_logo(self, driver_login, email, password):
        driver_login.find_element(*Locators.field_email_login).send_keys(email)
        driver_login.find_element(*Locators.field_password_login).send_keys(password)
        driver_login.find_element(*Locators.login_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        driver_login.find_element(*Locators.logo_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver_login.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_go_to_sauces_section(self, driver_login, email, password):

        driver_login.find_element(*Locators.field_email_login).send_keys(email)
        driver_login.find_element(*Locators.field_password_login).send_keys(password)
        driver_login.find_element(*Locators.login_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        driver_login.find_element(*Locators.sauces_section).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

    def test_go_to_fillings_section(self, driver_login, email, password):

        driver_login.find_element(*Locators.field_email_login).send_keys(email)
        driver_login.find_element(*Locators.field_password_login).send_keys(password)
        driver_login.find_element(*Locators.login_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        driver_login.find_element(*Locators.filling_section).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

    def test_go_to_buns_section(self, driver_login, email, password):

        driver_login.find_element(*Locators.field_email_login).send_keys(email)
        driver_login.find_element(*Locators.field_password_login).send_keys(password)
        driver_login.find_element(*Locators.login_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        driver_login.find_element(*Locators.sauces_section).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        driver_login.find_element(*Locators.buns_section).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))












