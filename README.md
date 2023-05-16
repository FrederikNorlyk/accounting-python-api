# Accounting API
Simple API for an accounting application, built using the Python framework Django.

## What can it do?
The application is modeled on an old PHP project, that I wrote to keep track of the expenses involved with restoring my sailboat. It keeps track of expenses, projects, and merchants.

## Why did i make this API?
In an attempt to learn Python and React I started working on this version. The API is the Python side of that attempt. Check out my other repository [accounting-react-frontend](https://github.com/FrederikNorlyk/accounting-react-frontend) which covers the React part.

## Try it out!
In a terminal navigate to the source code and run the following commands
```
python3 manage.py makemigrations accounting
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
