# Bitbucket API
Connecting to bitbucket api with a python script

### Requirements
* virtual environment
```
Install virtual environment: python3 -m pip install --user virtualenv
Create virtual environment: python3 -m venv virtual
Enter virtual environment: source virtual/bin/activate
Exit virtual environment: deactivate
```

* install dependancies
```
Enter virtual environment: source virtual/bin/activate
pip install -r requirements.txt
```

* [Create bitbucket OAuth](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html)

* [Create a Slack app and get the webhook URL](https://api.slack.com/incoming-webhooks)

* Create `.env` in root directory of the project

* Add the following information into your `.env`
```
KEY='<KEY>'
SECRET_KEY='<SECRET_KEY>'
USERNAME='<USERNAME>'
PASSWORD='<PASSWORD>'
POST_URL='<SlackWebhook>'
BITBUCKET_USERNAME='<Bitbucket_Username>'
REPOSLUG_LIST='<reposlug>'
```

### How to run
```
source virtual/bin/activate
pip install -r requirements.txt
To use get_access_token
    python bitbucket_api.py
To use other_get_access_token
    python bitbucket_api.py other
```
Running tests
```
pytest --v
```
Running tests with coverage
```
pytest -v --cov=bitbucket_api
```

### AoB
* updating `requirements.txt` with new installations
```
pip freeze > requirements.txt
```

### Interesting reads
* [Reading Environment Variables From .Env File In Python](https://robinislam.me/blog/reading-environment-variables-in-python/)
* [Installing packages using pip and virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
* [Requirements Files](https://pip.pypa.io/en/latest/user_guide/#requirements-files)
