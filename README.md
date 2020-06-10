




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

[![asciicast](https://asciinema.org/a/PuyuQDl1R1OrRkGWU6t5SblHo.svg)](https://asciinema.org/a/PuyuQDl1R1OrRkGWU6t5SblHo)


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

## Supported OS
Linux, MacOS

## 🌱 Contributing
Fell free to open issue and send pull request.


### startapp  supports Python >= 3.6
