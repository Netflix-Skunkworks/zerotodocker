#!/bin/bash

action=$1
cd /usr/local/src/sketchy

if [[ "$action" = "celery_api" ]]
then
    export C_FORCE_ROOT="true"
    celery worker -A sketchy.celery &
    gunicorn sketchy:app -b 0.0.0.0:8000
elif [[ "$action" = "api" ]]
then
    gunicorn sketchy:app -b 0.0.0.0:8000
elif [[ "$action" = "celery" ]]
then
    export C_FORCE_ROOT="true"
    celery worker -A sketchy.celery
elif [[ "$action" = "init_db" ]]
then
    sudo -u postgres psql -h sketchy_postgres --command "ALTER USER postgres with PASSWORD 'sketchypassword';"
    sudo -u postgres createdb -h sketchy_postgres -O postgres sketchy
    python manage.py create_db
fi
