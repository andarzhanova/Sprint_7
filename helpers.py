import requests
import random
import string


def generate_login_pass():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for i in range(length))
        return random_str

    login_pass = []
    while len(login_pass) != 3:
        random_string = generate_random_string(10)
        login_pass.append(random_string)

    return login_pass


def register_new_courier_and_return_login_password():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    return login_pass
