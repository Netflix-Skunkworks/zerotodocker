# Copyright 2014 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM ubuntu:14.04
MAINTAINER Netflix Open Source Development <talent@netflix.com>

ENV SECURITY_MONKEY_VERSION=v0.7.0  \
    SECURITY_MONKEY_SETTINGS=/usr/local/src/security_monkey/env-config/config-deploy.py

RUN apt-get update &&\
  apt-get -y -q install python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3 curl &&\
  apt-get install -y python-pip python-dev python-psycopg2 libffi-dev libpq-dev libyaml-dev libxml2-dev libxmlsec1-dev git sudo swig python-m2crypto &&\
  apt-get clean autoclean autoremove && rm -rf /var/lib/apt/lists/*

RUN cd /usr/local/src &&\
  git clone --branch $SECURITY_MONKEY_VERSION https://github.com/Netflix/security_monkey.git

RUN cd /usr/local/src/security_monkey &&\
  python setup.py install &&\
  /bin/mkdir -pv /var/log/security_monkey /usr/local/src/security_monkey/templates &&\
  touch /var/log/security_monkey/security_monkey-deploy.log /var/log/security_monkey/securitymonkey.log

ADD security_monkey-api/api-start.sh /usr/local/src/security_monkey/scripts/api-start.sh
ADD security_monkey-apiinit/api-init.sh /usr/local/src/security_monkey/scripts/api-init.sh
ADD security_monkey-scheduler/scheduler-start.sh /usr/local/src/security_monkey/scripts/scheduler-start.sh

RUN chmod +x /usr/local/src/security_monkey/scripts/*.sh

EXPOSE 5000

WORKDIR /usr/local/src/security_monkey
ENTRYPOINT ["/usr/local/src/security_monkey/scripts/api-start.sh"]

