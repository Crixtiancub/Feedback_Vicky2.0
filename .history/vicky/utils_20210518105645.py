import requests
import json
from prueba_Vicky.settings import URL_USUARIO   

def login_user():

    login = {
    "username":"1076506683",
    "password":"abcd.1234"
    }

    auto_user = json.loads(requests.post(url=URL_USUARIO,
    json=login).content)['access']

    return auto_user