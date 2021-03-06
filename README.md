Build a command line API client
===

|                                                                                                        Linter                                                                                                        |                                                                         CI/CD and testing                                                                         |                                                                                                Test Coverage                                                                                                 |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Thibault-Santonja/weather_api.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Thibault-Santonja/weather_api/context:python) | [![Build Status](https://circleci.com/gh/Thibault-Santonja/weather_api.svg?style=svg)](https://circleci.com/gh/Thibault-Santonja/weather_api) | [![Code Coverage](https://img.shields.io/codecov/c/github/Thibault-Santonja/weather_api.svg?style=for-the-badge)](https://codecov.io/github/Thibault-Santonja/weather_api?branch=master) |


## Subject
> Using the Metaweather API, make a command line tool that receives a city name as an
argument and says whether it’s going to rain tomorrow in this city or not. Here again,
packaging and tests are optional (but always appreciated). This can be done quite
shortly if you’re on a schedule and stick to the minimum.


## Installation
**Quick installation**:<br/>
```shell
make venv
source venv/Scripts/activate
```

**Without makefile installation**:<br/>
```shell
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

## Usage

**Using `python main.py <CITY>`**
![](https://i.imgur.com/8oo2QIj.png)

**Using `make weather-py CITY=<CITY>`**
![](https://i.imgur.com/c3y1rvG.png)

**Using `make weather CITY=<CITY>`**
![](https://i.imgur.com/kiUiqiK.png)


---
Thibault *Santonja*<br/>
*2022*
