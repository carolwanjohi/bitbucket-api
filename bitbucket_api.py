import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

def get_access_token(key, secret_key):
    # Using variables.
    print('key', key)
    print('secret_key',secret_key)

    response = requests.post('https://bitbucket.org/site/oauth2/access_token', auth=(key, secret_key))
    
    return response.json()

if __name__ == '__main__':
    # Get env file where SECRET and KEY are
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    
    # Accessing variables.
    key = os.getenv('KEY')
    secret_key = os.getenv('SECRET_KEY')

    # get access token
    access_token = get_access_token(key, secret_key)
    print('access_token', access_token)
