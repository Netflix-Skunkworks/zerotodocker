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

FROM netflixoss/java:8
MAINTAINER Netflix Open Source Development <talent@netflix.com>

RUN apt-get update &&\
  apt-get -y install ca-certificates &&\
  wget -q https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.64/bin/apache-tomcat-7.0.64.tar.gz.md5 &&\
  wget -q http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.64/bin/apache-tomcat-7.0.64.tar.gz &&\
  md5sum -c apache-tomcat-7.0.64.tar.gz.md5 &&\
  tar xzf apache-tomcat-7.0.64.tar.gz &&\
  rm /apache-tomcat-*.tar.gz* &&\
  mv /apache-tomcat-7.0.64 /tomcat &&\
  cd /tomcat/webapps &&\
  rm -Rf ROOT docs examples host-manager manager
  
EXPOSE 8080

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]
