# Accounting API
Simple API for an accounting application, built using the Python framework Django.

### What can it do?
The application is modeled on an old PHP project, that I wrote to keep track of the expenses involved with restoring my sailboat. It keeps track of expenses, projects, and merchants.

### Why did I make this API?
In an attempt to learn Python and React I started working on this application. The API is the Python side of that attempt. Check out my other repository [accounting-react-frontend](https://github.com/FrederikNorlyk/accounting-react-frontend) which covers the React part.

### Try it out!
In a terminal navigate to the source code and run the following commands
```
poetry install
pip install -r requirements.txt
python3 manage.py makemigrations accounting
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
You don't need to deploy the frontend application in order to try out the API, as it has its own web interface. Just open http://localhost:8000/ in your browser.
