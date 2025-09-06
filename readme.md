## create project ## 
## =================================================
## cd tutorial
## python -m venv env
## python -m pip install Django 
## django-admin startproject diis 
## -------------------------------------------------
## cd tutorial
## source env/bin/activate  # บน window ใช้ `env\Scripts\activate
## cd diis 
## run  :  python manage.py runserver
## ------------------------------------------------
## database configuration ## 
## =================================================
## pip install psycopg2-binary
## python manage.py makemigrations
## python manage.py migrate
