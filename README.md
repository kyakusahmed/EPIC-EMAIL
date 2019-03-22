[![Build Status](https://travis-ci.org/kyakusahmed/EPIC-EMAIL.svg?branch=challenge-2%2Fapi)](https://travis-ci.org/kyakusahmed/EPIC-EMAIL)
[![Coverage Status](https://coveralls.io/repos/github/kyakusahmed/EPIC-EMAIL/badge.svg?branch=challenge-2%2Fapi)](https://coveralls.io/github/kyakusahmed/EPIC-EMAIL?branch=challenge-2%2Fapi)
[![Maintainability](https://api.codeclimate.com/v1/badges/1b5054bcf77673c0fb3f/maintainability)](https://codeclimate.com/github/kyakusahmed/EPIC-EMAIL/maintainability)


# EPIC-EMAIL

 A web app that helps people exchange messages/information over the internet.
 
 [HEROKU](https://epemail.herokuapp.com/)
 
 [API DOCUMENTATION](https://epemail.herokuapp.com/apidocs/#/)

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

 open the terminal,activate virtual enviroment in the Root directory  and enter:
 ```
 $ pytest --cov
```


| tasks               |    URLS                |  METHOD  |         PARAMS                                | 
| ------------------- | -----------------------|----------|-----------------------------------------------|
|Create new account|api/v1/users/signup|POST| firstname,lastname,email,password|
|User signin|api/v1/users/login|GET| email,password|
|Get all user's recieved emails|api/v1/emails/users/received|GET| None|
|Get all unread emails for a user|/api/v1/emails/user/unread/<integer:id>|GET| id|
|Get all emails sent by a user|/api/v1/emails/user/sent/<integer:id>|GET| id|
|Get a specific user’s email|/api/v1/emails/specific-user/<integer:id>|GET| id|
|Send email to individuals|/api/v1/emails/user|POST| subject, message, status, sender_id, receiver_id, |
|Delete an email in a user’s inbox|/api/v1/emails/user/delete/<integer:id>|DELETE| id|


[GH-PAGES](https://kyakusahmed.github.io/EPIC-EMAIL/UI/signin.html)


Features as an Admin:

-   Create a group
-   Add different users to the group.

Features User side:

-   Signup page using personal credentials.
-   Login page using Email and Password.
-   Get all received emails for a user.
-   Get all unread emails for a user.
-   Get all emails sent by a user.
-   Get a specific user’s email.
-   Send email to individuals.
-   Delete an email in a user’s inbox.



