TO: create Project    
    django-admin startproject 'projectName' . {DONT FORGET => .}
TO: create app    
    python3 manage.py startapp todos
TO: create a new migrations file and then migrating the database with it
    python3 manage.py makemigrations "app name"
    python3 manage.py migrate "app name"
TO: create a superuser account so we can login to the admin.
    python3 manage.py createsuperuser
TO: start server
    python3 manage.py runserver
TO: run test cases
    python3 manage.py test