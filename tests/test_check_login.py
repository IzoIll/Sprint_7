import allure
import pytest
import requests

from helper import *
from data import *

@allure.description('Проверка ручки "Логин курьера в системе"')
class TestCheckLoginCourier:
    @allure.step('Вход в систему с существующими данными')
    def test_registration_and_login_courier(self):
        random_courier = generate_courier()
        requests.post(Urls.POST_COURIER, data=random_courier)
        response = requests.post(Urls.LOGIN_COURIER, data=random_courier)
        assert response.status_code == 200

    @allure.step('Вход в систему с несуществующим логином и паролем')
    def test_login_without_registration_courier(self):
        random_courier = generate_courier()
        response = requests.post(Urls.LOGIN_COURIER, data=random_courier)
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.step('Вход в систему без ввода логина')
    def test_login_without_registration_and_login_courier(self):
        random_courier = generate_courier_without_login()
        response = requests.post(Urls.LOGIN_COURIER, data=random_courier)
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.step('Вход в систему без ввода пароля')
    def test_login_without_registration_and_password_courier(self):
        random_courier = generate_courier_without_password()
        response = requests.post(Urls.LOGIN_COURIER, data=random_courier)
        assert response.json()['message'] == 'Недостаточно данных для входа'