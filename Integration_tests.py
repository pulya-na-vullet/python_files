from urllib import response
import requests
import json

Main_URL = 'https://reqres.in/api/'

#User list
response = requests.post(f'{Main_URL}users')
if response.status_code != 201:
    print(response.status_code, 'Faild.')

#Info one user 
response = requests.post(f'{Main_URL}users', data={'name': 'morpheus', 'job': 'leader'})
if response.status_code != 201:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.get(f'{Main_URL}users?delay=0')
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Response Text
response = requests.get(f'{Main_URL}users?delay=0')
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.delete(f'{Main_URL}users/2')
if response.status_code != 204:
    print(response.status_code, 'Faild.')

#Status Code 
response = requests.get(f'{Main_URL}unknown')
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Response Text
params_dict = {'q':'Python'}
response = requests.get(f'{Main_URL}unknown', params=params_dict)
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.get(f'{Main_URL}users?page=2')
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Response
params_dict = {'q':'Python'}
response = requests.get(f'{Main_URL}users?page=2', params=params_dict)
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.post(f'{Main_URL}login')
if response.status_code != 400:
    print(response.status_code, 'Faild.')

#Login
response = requests.post(f'{Main_URL}login', data={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'})
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.post(f'{Main_URL}login')
if response.status_code != 400:
    print(response.status_code, 'Faild.')

#Send Data
response = requests.post(f'{Main_URL}login', data={'email': 'peter@klaven'})
if response.status_code != 400:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.post(f'{Main_URL}register')
if response.status_code != 400:
    print(response.status_code, 'Faild.')

#Reg data (email, password)
response = requests.post(f'{Main_URL}register', data={'email': 'eve.holt@reqres.in', 'password': 'pistol'})
if response.status_code != 200:
    print(response.status_code, 'Faild.')
#Status Code
response = requests.post(f'{Main_URL}register')
if response.status_code != 400:
    print(response.status_code, 'Faild.')

#Send reg data
response = requests.post(f'{Main_URL}register', data={'email': 'sydney@fife'})
if response.status_code != 400:
    print(response.status_code, 'Faild.')

#Status code
response = requests.get(f'{Main_URL}unknown/23')
if response.status_code != 404:
    print(response.status_code, 'Faild.')

#Status Code 
response = requests.get(f'{Main_URL}unknown/2')
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Response Text
params_dict = {'q':'Python'}
response = requests.get(f'{Main_URL}unknown/2', params=params_dict)
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.get(f'{Main_URL}users/23')
if response.status_code != 404:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.get(f'{Main_URL}users/2')
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Response Text
params_dict = {'q': 'Python'}
response = requests.get(f'{Main_URL}users/2', params=params_dict)
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Status Code
response = requests.patch(f'{Main_URL}users/2')
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Data 
response = requests.patch(f'{Main_URL}users/2', data={'name': 'morpheus', 'job': 'zein resident'})
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Status code
response = requests.put(f'{Main_URL}users/2')
if response.status_code != 200:
    print(response.status_code, 'Faild.')

#Update data
response = requests.put(f'{Main_URL}users/2', data={'name': 'morpheus', 'job': 'zein resident'})
if response.status_code != 200:
    print(response.status_code, 'Faild.')