#!/bin/bash

action=$1
cd /usr/local/src/sketchy

if [[ "$action" = "api" ]]
then
    python manage.py create_db
    gunicorn sketchy:app -b 0.0.0.0:8000
elif [[ "$action" = "celery" ]]
then
    export C_FORCE_ROOT="true"
    celery worker -A sketchy.celery
fi
