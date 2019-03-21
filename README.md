# EPIC-EMAIL
 A web app that helps people exchange messages/information over the internet.

### How to run the app


Make sure that python 3.6 is installed on your computer

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
