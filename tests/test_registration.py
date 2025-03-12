import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers.locators import Locators
from helpers.generators import generate_name, generate_email, generate_password, generate_incorrect_password


class TestRegistration:

    def test_successful_registration(self, driver):
        name = generate_name()
        email = generate_email()
        password = generate_password()


        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.register_link))

        driver.find_element(*Locators.register_link).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.register_button))

        driver.find_element(*Locators.field_name_reg).send_keys(name)
        driver.find_element(*Locators.field_email_reg).send_keys(email)
        driver.find_element(*Locators.field_password_reg).send_keys(password)
        driver.find_element(*Locators.register_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.login_button))


        current_url = driver.current_url

        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_invalid_password_error(self, driver):
        name = generate_name()
        email = generate_email()
        password = generate_incorrect_password()

        driver.find_element(*Locators.account_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.register_link))

        driver.find_element(*Locators.register_link).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.register_button))

        driver.find_element(*Locators.field_name_reg).send_keys(name)
        driver.find_element(*Locators.field_email_reg).send_keys(email)
        driver.find_element(*Locators.field_password_reg).send_keys(password)
        driver.find_element(*Locators.register_button).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.incorrect_password_message))

        assert driver.find_element(*Locators.incorrect_password_message).text == "Некорректный пароль"






