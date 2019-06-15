import os
import requests
import json
import sys
from os.path import join, dirname
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

def get_user_input():
    if len(sys.argv) == 1:
        print("Will run get_access_token")
        return ''
    else:
        return sys.argv[1]

def select_method_to_get_access_token(method_selected):
    if method_selected == 'other':
        return other_get_access_token(key)
    else:
        return get_access_token(username, password, key, secret_key)

def get_access_token(username, password, key, secret_key):
    client = BackendApplicationClient(client_id={key})
    oauth = OAuth2Session(client=client)
    url = 'https://bitbucket.org/site/oauth2/access_token'
    response = oauth.fetch_token(url, username=username, password=password, auth=(key, secret_key))
    
    return response["access_token"]

def other_get_access_token(key):
    url = 'https://bitbucket.org/site/oauth2/authorize'
    params = {'client_id':key}
    response = requests.get(url, params)
    return response

def get_open_pull_requests(access_token):
    url = 'https://bitbucket.org/!api/2.0/pullrequests/carolwanjohi?'
    params = {'state': 'OPEN', 'access_token': access_token}
    response = requests.get(url, params)
    return response.json()

if __name__ == '__main__':
    # Get env file where SECRET and KEY are
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    
    # Accessing variables.
    key = os.getenv('KEY')
    secret_key = os.getenv('SECRET_KEY')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    # Get user input
    method_selected = get_user_input()
    print('method_selected', method_selected)

    # Get access token
    access_token = select_method_to_get_access_token(method_selected)    
    print('access_token', access_token)

    # Get Open PR
    open_pull_requests = get_open_pull_requests(access_token)
    print('open_pull_requests', open_pull_requests)
