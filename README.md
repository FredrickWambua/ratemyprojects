# Ratemyprojects
This is a clone for awwwards website from where users can submit their projects for others to view and vote on them.

## Author
Fredrick Wambua

## User Stories
- View posted projects and their details
- Post a project to be rated/reviewed
- Rate/ review other users' projects
- Search for projects 
- View projects overall score
- View my profile page

## Set up and Installation Requirements
### Prerequisites
- python 3.8
- django
- pipenv (for creating virtual environment)
- dotenv

## Technologies used
### To create a similar project, make use of relevant documentations
- Django Framework
- RESTful API
- Ajax
- Swagger for Api documentation
- Postman for testing the api endpoints

## Cloning the repository
- Fork the repository
```
$ git clone https://github.com/FredrickWambua/ratemyprojects
```
- Navigate to the repository.
### Running the application
- Creating virtual environment
```
$ python3 pipenv shell
$ pip freeze > requirements.txt
$ . .env
```
- Runing application
```
$ make server 
$ make makemigrations (this creates database migrations)
$ make migrate (this performs migrations)
$ make createsuperuser
```
## Known Bugs
Api authentication is currently not working

## Deployment
View the working deployed application [here](https://projectrating.herokuapp.com/)
Follow [heroku documentation](https://devcenter.heroku.com/articles/git) to know more about deploying app to heroku.

## License
Copyright 2021 Fredrick Wambua

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


