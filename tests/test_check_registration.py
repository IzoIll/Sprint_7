import requests
import allure

from helper import *
from data import *

@allure.description('Проверка ручки "Создание курьера"')
class TestCheckRegistrationCourier:
    @allure.title('Регистрация курьера')
    def test_registration_and_login_courier(self):
        random_courier = generate_courier()
        with allure.step("Отправляем запрос на регистрацию курьера"):
            response = requests.post(Urls.POST_COURIER, data=random_courier)
        assert response.json()['message'] == Answers.SUCCESS_REGISTRATION_COURIER['ok']
        assert response.status_code == Answers.SUCCESS_REGISTRATION_COURIER['code']

    @allure.title('Регистрация курьера с уже существующим логином')
    def test_registration_and_login_courier(self):
        random_courier = generate_courier()
        with allure.step("Отправляем запрос на регистрацию курьера"):
            requests.post(Urls.POST_COURIER, data=random_courier)
        with allure.step("Отправляем запрос на регистрацию второго курьера с такими же данными"):
            response = requests.post(Urls.POST_COURIER, data=random_courier)
        assert response.json()['message'] == Answers.LOGIN_IS_TAKEN['message']
        assert response.status_code == Answers.LOGIN_IS_TAKEN['code']

    @allure.title('Регистрация курьера без ввода логина')
    def test_login_without_registration_and_login_courier(self):
        random_courier = generate_courier_without_login()
        with allure.step("Отправляем запрос на регистрацию курьера без ввода логина"):
            response = requests.post(Urls.POST_COURIER, data=random_courier)
        assert response.json()['message'] == Answers.NOT_ENOUGH_DATA_REGISTRATION['message']
        assert response.status_code == Answers.NOT_ENOUGH_DATA_REGISTRATION['code']

    @allure.title('Регистрация курьера без ввода пароля')
    def test_login_without_registration_and_password_courier(self):
        random_courier = generate_courier_without_password()
        with allure.step("Отправляем запрос на регистрацию курьера без ввода пароля"):
            response = requests.post(Urls.POST_COURIER, data=random_courier)
        assert response.json()['message'] == Answers.NOT_ENOUGH_DATA_REGISTRATION['message']
        assert response.status_code == Answers.NOT_ENOUGH_DATA_REGISTRATION['code']