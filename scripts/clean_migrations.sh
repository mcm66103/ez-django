#!/bin/sh

find ../mywebdev -path "*/migrations/*.py" -not -name "__init__.py" -delete 

find ../mywebdev -path "*/migrations/*.pyc"  -delete

# python manage.py makemigrations

# python manage.py migrate

# read -sp 'seed db? y/n' seedDB

# if [ $seedDB = "y" ]
#   then
#   python manage.py loaddata datadump.json
# fi