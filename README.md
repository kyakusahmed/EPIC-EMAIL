[![Build Status](https://travis-ci.org/kyakusahmed/EPIC-EMAIL.svg?branch=challenge-2%2Fapi)](https://travis-ci.org/kyakusahmed/EPIC-EMAIL)
[![Coverage Status](https://coveralls.io/repos/github/kyakusahmed/EPIC-EMAIL/badge.svg?branch=challenge-2%2Fapi)](https://coveralls.io/github/kyakusahmed/EPIC-EMAIL?branch=challenge-2%2Fapi)
[![Maintainability](https://api.codeclimate.com/v1/badges/1b5054bcf77673c0fb3f/maintainability)](https://codeclimate.com/github/kyakusahmed/EPIC-EMAIL/maintainability)


# EPIC-EMAIL
 A web app that helps people exchange messages/information over the internet.

### How to run the app


Clone the repo
```
git clone https://github.com/kyakusahmed/EPIC-EMAIL.git
```
Change to the app directory
```
$ cd <app directory>
```
Create a virtual enviroment
```
virtualenv (name)
```
Activate the virtualenv
```
For Windows:
	$ (virtualenv name)\scripts\activate, and  	
For Linux: 
 	$source(virtualenv name)/bin/activate
```
Install the required modules from the requirements.txt file 
```
$ pip install -r requirements.txt
```
Run the app
```
$ python run.py
```


### How to run the Tests:

 open the terminal,activate virtual enviroment in the sendIT directory  and enter:
 ```
 $ pytest 
```


| tasks               |    URLS                |  METHOD  |         PARAMS                                | 
| ------------------- | -----------------------|----------|-----------------------------------------------|
|User signup|api/v1/users|POST|firstname,lastname,email,password|
|User signin|api/v1/users/login|GET|email,password|
| get all user's recieved emails|api/v1/emails/users/received|GET|None|
