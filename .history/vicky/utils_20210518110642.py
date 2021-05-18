import requests
import json
from prueba_Vicky.settings import URL_USUARIO   

import threading

def login_user():

    login = {
    "username":"1076506683",
    "password":"abcd.1234"
    }

    auto_user = json.loads(requests.post(url=URL_USUARIO,
    json=login).content)['access']

    return auto_user

def set_interval(func,time):
    e = threading.Event()
    while not e.wait(time):
        print("hola")
        func()  