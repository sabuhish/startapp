




# StartApp 

Simple boilerplate ready for development 

## Notes
- Currently supported  frameworks are:  FastApi, Flask

- Django coming soon...


### Installation ###

```sh
 $ sudo pip3 install startapp
```


### Guide

```bash

startapp 

```
```bash

for fastapi:

pipenv shell

export APP_SETTINGS=dev

pip install -requirements.txt or pipenv install

uvicorn app.main:app --reload --port 8007

for flask:

source .venv/bin/activate

pip install -requirements.txt

export FLASK_APP=app.app

export settings=dev

flask run

```

# Supported OS
Linux, MacOS

# Contributing
Fell free to open issue and send pull request.


### startapp  supports Python >= 3.6