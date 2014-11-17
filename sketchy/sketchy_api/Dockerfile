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

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 &&\
    echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list &&\
    apt-get update -y &&\
    apt-get -y -q install python-software-properties software-properties-common wget &&\
    apt-get -y -q install postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3 &&\
    apt-get install -y python-pip python-dev python-psycopg2 libpq-dev nginx supervisor git curl sudo &&\
    apt-get -y install libmysqlclient-dev libxslt-dev libxml2-dev libfontconfig1 &&\
    wget -O /usr/local/share/phantomjs-1.9.7-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2 &&\
        tar -xf /usr/local/share/phantomjs-1.9.7-linux-x86_64.tar.bz2 -C /usr/local/share/ &&\
        ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs


RUN cd /usr/local/src &&\
  git clone --depth 1 --branch master https://github.com/Netflix/sketchy.git &&\
  cd /usr/local/src/sketchy/ &&\
  python setup.py install

# Python logger seems to have seek errors when logging to stdout in thsi way.
#  ln -sf /dev/stdout /usr/local/src/sketchy/sketchy-deploy.log

ADD api-start.sh /usr/local/src/sketchy/scripts/api-start.sh
ADD config-default.py /usr/local/src/sketchy/config-default.py

RUN chmod 755 /usr/local/src/sketchy/scripts/api-start.sh

EXPOSE 8000

ENTRYPOINT ["/usr/local/src/sketchy/scripts/api-start.sh"]

CMD ["celery_api"]
