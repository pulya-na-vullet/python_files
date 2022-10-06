from unicodedata import name
from urllib import response
import requests
import json

Main_URL = 'https://reqres.in/api/'

#Список пользователей
response = requests.get(f'{Main_URL}users?page=2')
if response.status_code == 200:     print(response.status_code, 'Список пользователей OK')
elif response.status_code == 404:    print(response.status_code, 'Список пользователей Упс...')
print(response.text)

#Пользователь
response = requests.get(f'{Main_URL}users/2')
if response.status_code == 200:     print(response.status_code, 'Пользователь OK')
elif response.status_code == 404:    print(response.status_code, 'Пользователь Упс...')
print(response.text)

#Пользователь не найден
response = requests.get(f'{Main_URL}users/23')
if response.status_code == 200:     print(response.status_code, 'Пользователь не найден OK!')
elif response.status_code == 404:    print(response.status_code, 'Пользователь не найден Упс...')
print(response.text)

#Список ресурсов
response = requests.get(f'{Main_URL}unknown')
if response.status_code == 200:     print(response.status_code, 'Список ресурсов OK!')
elif response.status_code == 404:    print(response.status_code, 'Список ресурсов Упс...')
print(response.text)

#Первый ресурс
response = requests.get(f'{Main_URL}unknown/2')
if response.status_code == 200:     print(response.status_code, 'Первый ресурс OK!')
elif response.status_code == 404:    print(response.status_code, 'Первый ресурс Упс...')
print(response.text)

#Первый ресурс не найден
response = requests.get(f'{Main_URL}unknown/23')
if response.status_code == 200:     print(response.status_code, 'Первый ресурс не найден OK!')
elif response.status_code == 404:    print(response.status_code, 'Первый ресурс не найден Упс...')
print(response.text)

#Создание пользователя
response = requests.post(f'{Main_URL}users', data={'name': 'Bezumec', 'job': 'Tester'})
if response.status_code == 201:     print(response.status_code, 'Создание пользователя OK!')
elif response.status_code == 404:    print(response.status_code, 'Создание пользователя Упс...')
print(response.text)

#Обновление информации пользователя
response = requests.put(f'{Main_URL}users/2', data={'name': 'Bezumec', 'job': 'QA engineer'})
if response.status_code == 200:     print(response.status_code, 'Обновление информации пользователя OK!')
elif response.status_code == 404:    print(response.status_code, 'Обновление информации пользователя Упс...')
print(response.text)

#Обновление информации пользователя
response = requests.patch(f'{Main_URL}users/2', data={'name': 'Bezumec', 'job': 'QA engineer'})
if response.status_code == 200:     print(response.status_code, 'Обновление информации пользователя OK!')
elif response.status_code == 404:    print(response.status_code, 'Обновление информации пользователя Упс...')
print(response.text)

#Удаление
response = requests.delete(f'{Main_URL}users/2')
if response.status_code == 204:     print(response.status_code, 'Удаление OK!')
elif response.status_code == 404:    print(response.status_code, 'Удаление Упс...')
print(response.text)

#Регистрация пользователя
response = requests.post(f'{Main_URL}register', data={'email': 'eve.holt@reqres.in', 'password': 'pistol'})
if response.status_code == 200:     print(response.status_code, 'Регистрация пользователя OK!')
elif response.status_code == 404:    print(response.status_code, 'Регистрация пользователя Упс...')
print(response.text)

#Не успешная регистрация пользователя
response = requests.post(f'{Main_URL}register', data={'email': 'eve.holt@reqres.in'})
if response.status_code == 200:     print(response.status_code, 'Не успешная регистрация пользователя OK!')
elif response.status_code == 400:    print(response.status_code, 'Не успешная регистрация пользователя Упс...')
print(response.text)

#Авторизация пользователя
response = requests.post(f'{Main_URL}register', data={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
if response.status_code == 200:     print(response.status_code, 'Авторизация пользователя OK!')
elif response.status_code == 404:    print(response.status_code, 'Авторизация пользователя Упс...')
print(response.text)

#Не успешная авторизация пользователя
response = requests.post(f'{Main_URL}register', data={'email': 'eve.holt@reqres.in'})
if response.status_code == 200:     print(response.status_code, 'Не успешная авторизация пользователя OK!')
elif response.status_code == 400:    print(response.status_code, 'Не успешная авторизация пользователя Упс...')
print(response.text)

#Замедленная реакция ресурса
response = requests.get(f'{Main_URL}users?delay=3')
if response.status_code == 200:     print(response.status_code, 'Замедленная реакция ресурса OK!')
elif response.status_code == 404:    print(response.status_code, 'Замедленная реакция ресурса Упс...')
print(response.text)