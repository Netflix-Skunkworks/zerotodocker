#!/bin/bash

echo "Changing postgres password..."
sudo -u postgres psql -h postgres --command "ALTER USER postgres with PASSWORD 'password';"
echo "Done changing postgres password..."
echo "Creating sleepypuppydb....."
sudo -u postgres createdb -h postgres -O postgres sleepypuppydb
echo "DONE CREATING sleepypuppydb..."

cd /usr/local/src/sleepy-puppy
python manage.py setup_sleepy_puppy
gunicorn -w 4 -b 0.0.0.0:8000 sleepypuppy:app
