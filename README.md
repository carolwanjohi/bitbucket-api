# Bitbucket API
Connecting to bitbucket api with a python script

### Requirements
* virtual environment
```
* Install virtual environment: python3 -m pip install --user virtualenv
* Create virtual environment: python3 -m venv virtual
* Enter virtual environment: source virtual/bin/activate
* Exit virtual environment: deactivate
```

* dotenv
```
* Enter virtual environment: source virtual/bin/activate
pip install -U python-dotenv
```

* [Create bitbucket OAuth](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html)

* Create `.env` in root directory of the project

* Add the following information into your `.env`
```
KEY='<KEY>'
SECRET_KEY='<SECRET_KEY>'
```

### Interesting reads
* [Reading Environment Variables From .Env File In Python](https://robinislam.me/blog/reading-environment-variables-in-python/)