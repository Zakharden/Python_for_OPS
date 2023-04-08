import json
import requests

url = "https://httpbin.org"

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
        response = requests.post(url + "/post",
                                 params=querry_params,
                                 headers=headers,
                                 data=payload,
                                 files=files,
                                 timeout=0.0001 ) #Время ожидания ответа
    except requests.exceptions.ConnectTimeout:
        print("Ресурс недоступен")


# response = requests.get(url + "/get?param1=foo") #отпарвляем get запрос
#response = requests.get(url + "/get", params=querry_params, headers=headers)  # отпарвляем get запрос
#response = requests.post(url + "/post", params=querry_params, headers=headers, data = payload)  # отпарвляем post запрос
# print(response.status_code)  # выводит статус
#print(response.json())  # выводит получнный данные
# print(json.loads(response.text)) #из строки в словарь
# print(json.dumps(json.loads(response.text))) #обратно в строку


