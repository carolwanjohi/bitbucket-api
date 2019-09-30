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

def get_bitbucket_username():
    bitbucket_username = input("Enter bitbucket username: ")
    return bitbucket_username

def get_pull_request_status():
    pull_request_statuses = {1:'OPEN', 2:'MERGED', 3:'DECLINED', 4:'SUPERSEDED'}
    user_message = 'These are the avaiable pull request status\n1.{}\n2.{}\n3.{}\n4.{}\nEnter one of the pull request statuses: '.format(pull_request_statuses[1], pull_request_statuses[2], pull_request_statuses[3], pull_request_statuses[4])
    pull_request_status = input(user_message).upper()
    if pull_request_status in pull_request_statuses.values():
        return pull_request_status
    elif pull_request_status.isdigit() and int(pull_request_status) in pull_request_statuses.keys():
        return pull_request_statuses[int(pull_request_status)]
    else:
        print(str(pull_request_status)+" does not exist so get "+ pull_request_statuses[1]+" pull requests")
        return pull_request_statuses[1]

def format_pull_requests(pull_request_response):
    lines = []
    for i in pull_request_response['values']:
        line = '- *{0}* <{1}|{2}> - by {3}'.format(i['source']['branch']['name'],i['links']['html']['href'],i['title'],i['author']['display_name'])
        lines.append(line)
    return lines

def get_pull_requests(bitbbucket_username,pull_request_status,access_token):
    lines = []
    url = 'https://bitbucket.org/!api/2.0/pullrequests/'+bitbbucket_username+'?'
    params = {'state': pull_request_status, 'access_token': access_token}
    response = requests.get(url, params)
    pull_request_response = response.json()
    lines += format_pull_requests(pull_request_response)

    return pull_request_response

def send_to_slack(pr_list):
    for item in pr_list:
        text = item['links']['html']['href']
        author = item['author']['nickname']
        slack_msg = {
            'text': author + ': '+ text
        }
        response = requests.post(os.getenv('POST_URL'), headers={'Content-Type': 'application/json'},data=json.dumps(slack_msg))


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

    # Get bitbucket username
    bitbucket_username = get_bitbucket_username()
    print('bitbucket_username', bitbucket_username)

    # Get PR status
    pull_request_status = get_pull_request_status()
    print('pull_request_status', pull_request_status)

    # Get Open PR
    open_pull_requests = get_pull_requests(bitbucket_username,pull_request_status,access_token)
    print('pull_requests', open_pull_requests)

    #Send to Slack
    send_to_slack(open_pull_requests['values'])
