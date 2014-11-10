#!/bin/bash

cd /usr/local/src/security_monkey
export SECURITY_MONKEY_SETTINGS=`pwd`/env-config/config-deploy.py
python manage.py run_change_reporter all
python manage.py start_scheduler

