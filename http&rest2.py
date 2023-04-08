import json
import requests

url = "https://httpbin.org"
session = requests.Session() #чтобы не закрывалось соединение

querry_params = {
    "param1": "foo",
    "param2": "bar"
}
headers = {
    "User-Agent": "Chrome",
    "Authorization": "Bearer: jdasuhfgvyuidsgf",
}

payload = {
    "id": 23142,
    "name": "Python"
}
"""Отпарвка данный из файла"""
with open("test.txt") as text_file:
    files ={
        "text_file": text_file
    }
    try:
        response = session.post(url + "/post",
                                 params=querry_params,
                                 headers=headers,
                                 data=payload,
                                 files=files,
                                 timeout=10.0001 ) #Время ожидания ответа
    except requests.exceptions.ConnectTimeout:
        print("Ресурс недоступен")


print(response.status_code)  # выводит статус
print(json.loads(response.text)) #из строки в словарь



