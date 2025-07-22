from faker import Faker

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