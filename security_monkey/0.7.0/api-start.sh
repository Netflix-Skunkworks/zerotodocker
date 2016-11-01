#!/bin/bash

cd /usr/local/src/security_monkey/
exec python manage.py run_api_server -b 0.0.0.0:${SECURITY_MONKEY_API_PORT:-5000}
