"""API """
import requests
import os

API_URL = os.getenv('API_URL', None)
JWT_TOKEN = os.getenv('JWT', None)
EXECUTION_ID = os.getenv('EXECUTION_ID', None)

HEADERS = {'Authorization': 'Bearer ' + JWT_TOKEN}


def patch_execution(json):
    response = requests.patch(API_URL + '/api/v1/execution/'+ EXECUTION_ID, json=json, headers=HEADERS)
    if response.status_code != 200:
        print('Error doing request.')
        print(response)

def save_log(json):
    response = requests.post(API_URL + '/api/v1/execution/'+ EXECUTION_ID + '/log', json=json, headers=HEADERS)
    if response.status_code != 200:
        print('Error doing request.')
        print(response)
