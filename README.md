# COW API

A FLASK REST API for the application.

## Prerequisites

Ensure you have Postgres, Python 3.5 and above and virtualenv installed on your machine.

## Setting up

* Clone repository to your working directory
```bash
$ git clone https://github.com/naibor/Cow.git
```

* Switch to the `api` directory
```bash
$ cd api/
```

* Activate virtual environment Install app dependencies
```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
*Set up the database
```
environment:
        POSTGRES_USER: postgress
        PASSWORD:password
        POSTGRES_DB: cow
```
```bash
. venv/bin/activate
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade

* Run application
```bash
$ python run.py
```
