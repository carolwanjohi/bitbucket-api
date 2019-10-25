import os
import requests
import json
import csv
from os.path import join, dirname
from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from datetime import date, timedelta,datetime


def select_method_to_get_access_token():

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


def format_pull_requests(pull_request_response):
    lines = []

    for pull_request in pull_request_response:
        line = '"{0}""{1}""{2}""{3}"'.format(pull_request.get('source',{}).get('branch').get('name'),pull_request.get('links').get('html').get('href'),pull_request.get('title'),pull_request.get('author').get('display_name'))
        lines.append(send_to_slack(line))
    return lines


def format_repo_slug_list(repo_slug_response):
    lines = []
    for i in repo_slug_response['values']:
        line = '- *{0}* <{1}|{2}> - by {3}'.format(i['source']['branch']['name'],i['links']['html']['href'],i['title'],i['author']['display_name'])
        lines.append(line)
    return lines


def get_pull_requests(bitbbucket_username,repo_slug,access_token):
    lines = []
    url = 'https://api.bitbucket.org/2.0/repositories/'+ bitbbucket_username + '/' + repo_slug + '/pullrequests?q=state="OPEN"'
    params = {'access_token': access_token}
    response = requests.get(url, params)
    pull_request_response = response.json()
    pull_request_response_list = []
    for pull_request_response in pull_request_response.get('values'):
        date_string = pull_request_response.get('updated_on')
        date_object = datetime.strptime(date_string,'%Y-%m-%dT%H:%M:%S.%f+00:00').date()
        if date_object < ((date.today()-timedelta(days=2))):
            pull_request_response_list.append(pull_request_response)
    lines.append(format_pull_requests(pull_request_response_list))

    return pull_request_response


def get_repo_slug(bitbucket_username):
    url='https://api.bitbucket.org/2.0/repositories/'+ bitbucket_username
    params = {'access_token': access_token}
    response = requests.get(url, params)
    return response.json()


def send_to_slack(pull_request_response):
    print("slack",(pull_request_response))
    parser = list(csv.reader(pull_request_response))
    for pull_request in parser:
        for i,f in enumerate(pull_request):
            print(i,f)
            branch_name = parser[0]
            pull_request_link = parser[1]
            pull_request_name =parser[2]
            author = parser[3]
            slack_msg = {'text':"Branch Name:"+ str(branch_name)+"\nLink:"+str(pull_request_link)+"\nPull Request:"+str(pull_request_name)+"\nAuthor:"+str(author) }
            response = requests.post(os.getenv('POST_URL'), headers={'Content-Type': 'application/json'},data=json.dumps(slack_msg))
            print(slack_msg)


if __name__ == '__main__':
    # Get env file where SECRET and KEY are
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    # Accessing variables.
    key = os.getenv('KEY')
    secret_key = os.getenv('SECRET_KEY')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    # Get access token
    access_token = select_method_to_get_access_token()
    print('access_token', access_token)

    #Get List of Reposlug
    repo_slug_response=get_repo_slug(os.getenv('BITBUCKET_USERNAME'))
    repo_slug_list = []
    for repo_slug in repo_slug_response.get('values'):
        repo_slug_list.append(repo_slug.get('slug'))

    # Get Open PR
    for i in repo_slug_list:
       open_pull_requests = get_pull_requests(os.getenv('BITBUCKET_USERNAME'),i,access_token)
    # print('pull_requests', open_pull_requests)

    #Send to Slack
    send_to_slack(open_pull_requests)
    print(open_pull_requests)
