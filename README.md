




# StartApp 

Simple boilerplate ready for development 

[![MIT licensed](https://img.shields.io/github/license/marlin-dev/startapp)](https://raw.githubusercontent.com/marlin-dev/startapp/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/marlin-dev/startapp.svg)](https://github.com/marlin-dev/startapp/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/marlin-dev/startapp.svg)](https://github.com/marlin-dev/startapp/network)
[![GitHub issues](https://img.shields.io/github/issues-raw/marlin-dev/startapp)](https://github.com/marlin-dev/startapp/issues)
[![Downloads](https://pepy.tech/badge/startapp)](https://pepy.tech/project/startapp)


## Notes
- Currently supported  frameworks are:  FastApi, Flask




###  🔨  Installation ###

```sh
 $ sudo pip3 install startapp
```


### 🕹 Guide

```bash

startapp  --help 

```
- Type  startapp  on terminal press enter, questions will promt on terminal choose accroding to your taste.



```bash

Right after your choice do the followings accrodingly: 

for fastapi:

source .venv/bin/activate


export settings=dev

pip install -r requirements.txt 

uvicorn app.main:app --reload --port 8007

for flask:

source .venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=app.app

export settings=dev

flask run

```
Flask Structure

```bash 
├── app
│   ├── controllers
│   │   ├── app.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── models.py
│   ├── serializers
│   │   ├── __init__.py
│   │   └── serializer.py
│   └── utils.py
├── app_init
│   ├── app_factory.py
│   ├── __init__.py
│   
│       
│       
├── extensions
│   ├── db_conf.py
│   ├── extension.py
│   ├── __init__.py
│   
│       
│       
├── prestart.sh
├
│   
├── README.md
├── requirements.txt
├── server.py
├── settings
│   ├── devsettings.py
│   ├── prodsettings.py
│   ├── settings.py
│   └── testsettings.py
└── tests
    ├── __init__.py
    └── test.py

```

FastApi Structure
```bash
├── app
│   ├── controllers
│   │   ├── controller
│   │   │   ├── controller.py
│   │   │   └── schemas.py
│   │   └── __init__.py
│   ├── data
│   │   ├── __init__.py
│   │   └── models.py
│   ├── __init__.py
│   ├── main.py
│   └── utils
│       ├── helpers.py
│       └── __init__.py
├── container.sh
├── core
│   ├── dbsetup.py
│   ├── extensions.py
│   ├── factories.py
│   ├── __init__.py
│   └── settings
│       ├── devsettings.py
│       ├── __init__.py
│       ├── prodsettings.py
│       └── settings.py
├── Dockerfile
├── prestart.sh
├── README.md
├── req.txt
├── requirements.txt
└── start.sh


```

## Supported OS
Linux, MacOS

## 🌱 Contributing
Fell free to open issue and send pull request.


### startapp  supports Python >= 3.6
