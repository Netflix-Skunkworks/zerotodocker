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

FROM netflixoss/tomcat:7
MAINTAINER Netflix Open Source Development <talent@netflix.com>

RUN cd /tomcat/webapps &&\
  mkdir ROOT &&\
  cd ROOT &&\
  wget -q http://repo1.maven.org/maven2/com/netflix/zuul/zuul-netflix-webapp/1.0.28/zuul-netflix-webapp-1.0.28.war &&\
  jar xf zuul-netflix-webapp-1.0.28.war &&\
  rm zuul-netflix-webapp-1.0.28.war

ADD config.properties /tomcat/webapps/ROOT/WEB-INF/classes/config.properties
ADD zuul-test.properties /tomcat/webapps/ROOT/WEB-INF/classes/zuul-test.properties
  
EXPOSE 8080

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]
