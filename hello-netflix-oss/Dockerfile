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
  wget -q http://repo1.maven.org/maven2/com/netflix/karyon/hello-netflix-oss/1.0.27/hello-netflix-oss-1.0.27.war &&\
  jar xf hello-netflix-oss-1.0.27.war &&\
  rm hello-netflix-oss-1.0.27.war &&\
  rm WEB-INF/classes/hello-netflix-oss-dev.properties &&\
  rm WEB-INF/classes/hello-netflix-oss.properties &&\
  rm WEB-INF/classes/eureka-client.properties

ADD config.properties /tomcat/webapps/ROOT/WEB-INF/classes/config.properties
ADD hello-netflix-oss.properties /tomcat/webapps/ROOT/WEB-INF/classes/hello-netflix-oss.properties
ADD hello-netflix-oss-test.properties /tomcat/webapps/ROOT/WEB-INF/classes/hello-netflix-oss-test.properties
  
EXPOSE 8080 8077

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]
