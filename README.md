# Автоматизированные тесты для веб-приложения

## Описание
Этот репозиторий содержит автоматизированные тесты для проверки функциональности веб-приложения. Тесты написаны на Python с использованием библиотеки Selenium и pytest.

## Структура проекта
```
tests/                        # Корневая папка с тестами
│
├── test_registration.py       # Тесты регистрации
│   ├── class TestRegistration:
│   │   ├── test_successful_registration(self)  # Проверка успешной регистрации
│   │   ├── test_invalid_password_error(self)   # Проверка ошибки при вводе некорректного пароля
│
├── test_login.py              # Тесты входа в систему
│   ├── class TestLogin:
│   │   ├── test_login_from_main_page(self)            # Логин с главной страницы
│   │   ├── test_login_from_personal_account(self)     # Логин из личного кабинета
│   │   ├── test_login_from_registration_form(self)    # Логин из формы регистрации
│   │   ├── test_login_from_password_recovery_form(self) # Логин из формы восстановления пароля
│
├── test_personal_account.py    # Тесты личного кабинета
│   ├── class TestPersonalAccount:
│   │   ├── test_go_to_personal_account(self)   # Переход в личный кабинет
│   │   ├── test_logout_from_personal_account(self) # Выход из личного кабинета
│
├── test_constructor.py         # Тесты раздела "Конструктор"
│   ├── class TestConstructor:
│   │   ├── test_go_to_constructor_from_personal_account(self) # Переход в конструктор из ЛК
│   │   ├── test_go_to_constructor_by_logo(self)               # Переход в конструктор по логотипу
│   │   ├── test_go_to_buns_section(self)                      # Проверка перехода в раздел "Булки"
│   │   ├── test_go_to_sauces_section(self)                    # Проверка перехода в раздел "Соусы"
│   │   ├── test_go_to_fillings_section(self)                  # Проверка перехода в раздел "Начинки"
```

## Установка и настройка
### 1. Клонирование репозитория
```sh
git clone <репозиторий>
cd <папка_проекта>
```
### 2. Создание виртуального окружения и установка зависимостей
```sh
python -m venv .venv
source .venv/bin/activate  # Для macOS/Linux
.venv\Scripts\activate     # Для Windows
pip install -r requirements.txt
```

## Используемые технологии
- Python
- Selenium WebDriver
- Pytest

## Авторы
Разработчик тестов: Шакмаев Тимур

