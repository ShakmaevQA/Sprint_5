import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators


class TestLogin:
    def test_login_via_main_page(self, driver, email, password):

        driver.find_element(*Locators.login_button_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.login_button))

        driver.find_element(*Locators.field_email_login).send_keys(email)
        driver.find_element(*Locators.field_password_login).send_keys(password)
        driver.find_element(*Locators.login_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_from_personal_account(self, driver_login, email, password):

        driver_login.find_element(*Locators.field_email_login).send_keys(email)
        driver_login.find_element(*Locators.field_password_login).send_keys(password)
        driver_login.find_element(*Locators.login_button).click()
        WebDriverWait(driver_login, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver_login.current_url == 'https://stellarburgers.nomoreparties.site/'


    def test_login_from_registration_form(self, driver_register, email, password):

        driver_register.find_element(*Locators.login_button_reg).click()
        WebDriverWait(driver_register, 6).until(expected_conditions.visibility_of_element_located(Locators.login_button))

        driver_register.find_element(*Locators.field_email_login).send_keys(email)
        driver_register.find_element(*Locators.field_password_login).send_keys(password)
        driver_register.find_element(*Locators.login_button).click()
        WebDriverWait(driver_register, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver_register.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_from_password_recovery_form(self, driver_forgot_password, email, password):

        driver_forgot_password.find_element(*Locators.login_button_recovery).click()
        WebDriverWait(driver_forgot_password, 6).until(expected_conditions.visibility_of_element_located(Locators.login_button))

        driver_forgot_password.find_element(*Locators.field_email_login).send_keys(email)
        driver_forgot_password.find_element(*Locators.field_password_login).send_keys(password)
        driver_forgot_password.find_element(*Locators.login_button).click()
        WebDriverWait(driver_forgot_password, 6).until(expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver_forgot_password.current_url == 'https://stellarburgers.nomoreparties.site/'


