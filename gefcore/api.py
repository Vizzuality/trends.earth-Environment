"""API """
import requests
import os

API_URL = os.getenv('API_URL', None)
EMAIL = os.getenv('EMAIL', None)
PASSWORD = os.getenv('PASSWORD', None)
EXECUTION_ID = os.getenv('EXECUTION_ID', None)

def login():
    response = requests.post(API_URL + '/auth', json={"email":EMAIL, "password": PASSWORD })
    if response.status_code != 200:
        print('Error login.')
        print(response)
        raise Exception('Error login')
    return response.json().access_token

def patch_execution(json):
    jwt = login()

    response = requests.patch(API_URL + '/api/v1/execution/'+ EXECUTION_ID, json=json, headers={'Authorization': 'Bearer ' + jwt})
    if response.status_code != 200:
        print('Error doing request.')
        print(response)

def save_log(json):
    response = requests.post(API_URL + '/api/v1/execution/'+ EXECUTION_ID + '/log', json=json, headers={'Authorization': 'Bearer ' + jwt})
    if response.status_code != 200:
        print('Error doing request.')
        print(response)
