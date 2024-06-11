from faker import Faker


def register_new_courier():
    fake = Faker()
    login = fake.user_name()
    password = fake.password()
    first_name = fake.name()
    reg_data = {
        "login": login,
        "password": password,
        "name": first_name
    }
    return reg_data


def register_new_courier_without_login():
    fake = Faker()
    password = fake.password()
    first_name = fake.name()
    reg_data = {
        "password": password,
        "name": first_name
    }
    return reg_data


def register_new_courier_without_password():
    fake = Faker()
    login = fake.user_name()
    first_name = fake.name()
    reg_data = {
        "login": login,
        "name": first_name
    }
    return reg_data
