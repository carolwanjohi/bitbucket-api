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

* Create `.env` in root directory of the project

* Add the following information into your `.env`
```
KEY='<KEY>'
SECRET_KEY='<SECRET_KEY>'
USERNAME='<USERNAME>'
PASSWORD='<PASSWORD>'
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