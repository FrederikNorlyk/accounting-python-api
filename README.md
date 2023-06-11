# Accounting API
Simple API for an accounting application, built using the Python framework Django.

### Technologies
- Python 3.10
- Django (Django REST framework)

### What can it do?
The application is modeled on an old PHP project, that I wrote to keep track of the expenses involved with restoring my sailboat. It keeps track of expenses, projects, and merchants.

### Why did I make this API?
In an attempt to learn Python and React I started working on this application. The API is the Python side of that attempt. Check out my other repository [accounting-react-frontend](https://github.com/FrederikNorlyk/accounting-react-frontend) which covers the React part.

### Try it out!
The project is hosted [here on Render](https://accounting-api-42y3.onrender.com). Beware that it is running on their free tier which is quite slow. The first time you visit the address, Render will spin up the server, so please be patient. When creating a new user some random demo data is generated.

### Run it yourself ###
In a terminal, navigate to the root directory and run the following commands
```
poetry install
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
You don't need to deploy the frontend application in order to try out the API, as it has its own web interface. Just open http://localhost:8000/ in your browser.
