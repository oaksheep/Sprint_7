class Users:
    data_current = {
        "login": "lida123",
        "password": "lida123"
    }
    data_negative = {
        "login": "lida123",
        "password": "incorrect"
    }
    data_without_login = {
        "login": "",
        "password": "lida123"
    }
    data_without_password = {
        "login": "lida123",
        "password": ""
    }


class Orders:
    data_order = {
        "firstName": "Lida",
        "lastName": "Oaksheep",
        "address": "Nevskiy, 1",
        "metroStation": 5,
        "phone": "+7 921 558 83 49",
        "rentTime": 6,
        "deliveryDate": "2024-06-15",
        "comment": "I want samokat",
        "color": [
            "BLACK"
        ]
    }
