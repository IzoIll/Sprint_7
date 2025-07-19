import requests

from faker import Faker
from data import Urls

def generate_courier():
    return {
    "login": Faker().name(),
    "password": Faker().password(),
    "firstName": Faker().first_name()
    }

def generate_courier_without_login():
    return {
    "login": '',
    "password": Faker().password(),
    "firstName": Faker().first_name()
    }

def generate_courier_without_password():
    return {
    "login": Faker().name(),
    "password": '',
    "firstName": Faker().first_name()
    }

def generate_courier_without_firstName():
    return {
    "login": Faker().name(),
    "password": Faker().password(),
    "firstName": ''
    }

def registration_courier():
    login_pass = generate_courier()
    requests.post(Urls.POST_COURIER, data=generate_courier())
    return login_pass