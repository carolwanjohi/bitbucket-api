import os
import requests
import json
from os.path import join, dirname
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient

def get_access_token(username, password, key, secret_key):
    # Using variables.
    print('username', username)
    print('password', password)
    print('key', key)
    print('secret_key',secret_key)
    client = BackendApplicationClient(client_id={key})
    oauth = OAuth2Session(client=client)
    url = 'https://bitbucket.org/site/oauth2/access_token'
    response = oauth.fetch_token(url, username=username, password=password, auth=(key, secret_key))
    
    return response["access_token"]

if __name__ == '__main__':
    # Get env file where SECRET and KEY are
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    
    # Accessing variables.
    key = os.getenv('KEY')
    secret_key = os.getenv('SECRET_KEY')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    # get access token
    access_token = get_access_token(username, password, key, secret_key)
    print('access_token', access_token)
