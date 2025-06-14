# Auth-and-User-Management-Microservice
This microservice handles user registration and login/logout, authentication, password storage, profile management, Role Based Access Control. 

**The service is meant to be reused for different applications**


## Set up and Running
To setup the application, create a copy of the example.env and rename it as .env

Fill the values in the .env

To run the application:

`pip install pipenv`

`pipenv shell`

`pipenv install`

`pipenv run uvicorn app.main:app --reload`
