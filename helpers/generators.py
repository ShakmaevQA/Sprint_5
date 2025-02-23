import random


def generate_password():
    return ''.join(str(random.randint(0, 9)) for _ in range(8))

def generate_email():
        random_digits = random.randint(100, 999)
        random_user_email = f"timurshakmaev{random_digits}@yandex.ru"
        return random_user_email

def generate_name():
        first_names = ["Иван", "Петр", "Олег"]
        last_names = ["Иванов", "Петров", "Краснов"]
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        random_user_name = f"{first_name} {last_name}"
        return random_user_name

def generate_incorrect_password():
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

