import requests
from fns.constants import *


class FnsApi:
    @staticmethod
    def login(phone, password):
        return requests.get(URL_LOGIN, auth=("+7" + phone, password))

    @staticmethod
    def register(phone, email, name):
        json = {
            "phone": "+7" + phone,
            "email": email,
            "name": name,
        }
        return requests.post(URL_REGISTRATION, headers=HEADERS, json=json)

    @staticmethod
    def restore(phone):
        json = {
            "phone": "+7" + phone,
        }
        return requests.post(URL_RESTORE, headers=HEADERS, json=json)

    @staticmethod
    def receipt_existing(fn, n, i, fp, date, amount):
        return requests.get(URL_RECEIPT_EXIST.format(fn, n, i, fp, date, amount))

    @staticmethod
    def receive(phone, password, fn, i, fp):
        get_receipt_url = URL_RECEIVE.format(fn, i, fp)

        # если запрашивать чек впервые, то он приходит только с третьей попытки
        for i in range(3):
            result = requests.get(get_receipt_url, auth=("+7" + phone, password), headers=HEADERS)
            if result.status_code == 200:
                return result
        return result
