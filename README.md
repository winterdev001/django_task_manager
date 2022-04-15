# Application for task management

This application allows users to register task information such as title, description, status and due date.

Tasks have mandatory entry of title and due date, and validation that the due date is after today.

[![Image from Gyazo](https://i.gyazo.com/9236223485fc8a966d79bc394c15daac.gif)](https://i.gyazo.com/9236223485fc8a966d79bc394c15daac)

## Commands for building environment
```bash
pip install -r requirements.txt
createdb task_manager
python manage.py migrate
python manage.py runserver
```

## Version used
```
asgiref==3.5.0
Django==4.0
sqlparse==0.4.2
tzdata==2022.1
