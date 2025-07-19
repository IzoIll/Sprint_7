import allure
import pytest
import requests

from helper import *
from data import *

@allure.description('Проверка ручки "Создание курьера"')
class TestCheckRegistrationCourier:
    @allure.step('Регистрация курьера')
    def test_registration_and_login_courier(self):
        random_courier = generate_courier()
        response = requests.post(Urls.POST_COURIER, data=random_courier)
        assert response.json() == {'ok': True}

    @allure.step('Регистрация курьера с уже существующим логином')
    def test_registration_and_login_courier(self):
        random_courier = generate_courier()
        requests.post(Urls.POST_COURIER, data=random_courier)
        response = requests.post(Urls.POST_COURIER, data=random_courier)
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.step('Регистрация курьера без ввода логина')
    def test_login_without_registration_and_login_courier(self):
        random_courier = generate_courier_without_login()
        response = requests.post(Urls.POST_COURIER, data=random_courier)
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.step('Регистрация курьера без ввода пароля')
    def test_login_without_registration_and_password_courier(self):
        random_courier = generate_courier_without_password()
        response = requests.post(Urls.POST_COURIER, data=random_courier)
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'