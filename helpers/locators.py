from selenium.webdriver.common.by import By


class Locators:
    # Кнопка "Личный кабинет"
    account_button = By.XPATH, './/p[text() = "Личный Кабинет"]'
    # Активный ссылка: "Зарегистрироваться"
    register_link = (By.XPATH, './/a[text() = "Зарегистрироваться"]')
    # Кнопка "Зарегистрироваться"
    register_button = (By.XPATH, './/button[text() = "Зарегистрироваться"]')
    # Поле "Имя" для экрана регистрации
    field_name_reg = By.XPATH, './/label[contains(text(), "Имя")]/following-sibling::input'
    # Поле "Email" для экрана регистрации
    field_email_reg = By.XPATH, './/label[contains(text(), "Email")]/following-sibling::input'
    # Поле "Пароль" для экрана регистрации
    field_password_reg = By.XPATH, './/label[contains(text(), "Пароль")]/following-sibling::input'
    # Кнопка "Сохранить"
    save_button = By.XPATH, './/button[2][text() = "Сохранить"]'
    # Кнопка "Оформить заказ"
    order_button = By.XPATH, './/button[text()="Оформить заказ"]'
    # Поле "Email" на экране авторизации
    field_email_login = By.XPATH, './/input[@name = "name"]'
    # Поле "Пароль" на экране авторизации
    field_password_login = By.XPATH, './/input[@name = "Пароль"]'
    # Кнопка "Войти" на экране авторизации
    login_button = By.XPATH, './/button[text() = "Войти"]'
    # Текст валидации при вводе некорректного пароля
    incorrect_password_message = By.XPATH, './/p[text() = "Некорректный пароль"]'
    # Кнопка "Войти в аккаунт" в рамках главного экрана
    login_button_main = By.XPATH, './/button[text() = "Войти в аккаунт"]'
    # Кнопка "Войти" на форме регистрации
    login_button_reg = By.XPATH, './/a[text() = "Войти"]'
    # Кнопка "Войти" на форме восстановления пароля
    login_button_recovery = By.XPATH, './/a[text() = "Войти"]'
    # Кнопка "Выйти" в личном кабинете
    logout_button = By.XPATH, './/button[text()="Выход"]'
    # Кнопка "Конструктор"
    constructor_button = By.XPATH, '//p[text() = "Конструктор"]'
    # Логотип Stellar Burgers
    logo_button = By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]'
    # Раздел "Булки"
    buns_section = By.XPATH, './/span[text() = "Булки"]'
    # Раздел "Соусы"
    sauces_section = By.XPATH, '//span[text() = "Соусы"]'
    # Раздел "Начинки"
    filling_section = By.XPATH, '//span[text() = "Начинки"]'






