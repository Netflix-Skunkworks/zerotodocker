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

ENV CATALINA_OPTS="-Dspring.profiles.active=prod -Darchaius.deployment.applicationId=genie2 -Darchaius.deployment.environment=dev"

RUN wget -q -P /tomcat/webapps 'http://repo1.maven.org/maven2/com/netflix/genie/genie-web/2.0.0/genie-web-2.0.0.war' &&\
  mkdir /tomcat/webapps/ROOT &&\
  cd /tomcat/webapps/ROOT &&\
  jar xf ../genie-web-2.0.0.war &&\
  cd .. &&\
  rm genie-web-2.0.0.war &&\
  mkdir /tomcat/webapps/genie-jobs

RUN mkdir /tmp/genie-server &&\
  cp /tomcat/webapps/ROOT/WEB-INF/lib/genie-server-2.0.0.jar /tmp/genie-server/ &&\
  cd /tmp/genie-server/ &&\
  jar xf genie-server-2.0.0.jar &&\
  rm genie-server-2.0.0.jar &&\
  sed -i 's/127.0.0.1/mysql-genie/' genie-jpa.xml &&\
  sed -i 's/name="password" value=""/name="password" value="genie"/' genie-jpa.xml &&\
  jar cf genie-server-2.0.0.jar * &&\
  mv genie-server-2.0.0.jar /tomcat/webapps/ROOT/WEB-INF/lib/ &&\
  cd /tomcat &&\
  rm -rf /tmp/genie-server

RUN sed -i 's/netflix.appinfo.port=7001/netflix.appinfo.port=8080/' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i 's/netflix.appinfo.name=genie/netflix.appinfo.name=genie2/' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i 's/netflix.genie.server.user.working.dir=\/mnt\/tomcat\/genie-jobs/netflix.genie.server.user.working.dir=\/tomcat\/webapps\/genie-jobs/' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i 's/netflix.genie.server.java.home=\/usr\/lib\/jvm\/java-6-sun/netflix.genie.server.java.home=\/usr\/lib\/jvm\/java-7-oracle/' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties

RUN wget -q -P /tomcat/conf 'https://raw.githubusercontent.com/Netflix/genie/2.0.0/genie-web/conf/system/apps/tomcat/conf/listings.xsl'

RUN mkdir -p /apps/genie/bin &&\
  wget -q -P /apps/genie/bin 'https://raw.githubusercontent.com/Netflix/genie/2.0.0/genie-web/conf/system/apps/genie/bin/jobkill.sh' &&\
  chmod 755 /apps/genie/bin/jobkill.sh &&\
  wget -q -P /apps/genie/bin 'https://raw.githubusercontent.com/Netflix/genie/2.0.0/genie-web/conf/system/apps/genie/bin/joblauncher.sh' &&\
  chmod 755 /apps/genie/bin/joblauncher.sh &&\
  wget -q -P /apps/genie/bin 'https://raw.githubusercontent.com/Netflix/genie/2.0.0/genie-web/conf/system/apps/genie/bin/localCleanup.py' &&\
  chmod 755 /apps/genie/bin/localCleanup.py &&\
  wget -q -P /apps/genie/bin 'https://github.com/Netflix/genie/blob/2.0.0/genie-web/conf/system/apps/genie/bin/timeout3' &&\
  chmod 755 /apps/genie/bin/timeout3
  

EXPOSE 8080

ENTRYPOINT ["/tomcat/bin/catalina.sh"]
#ENTRYPOINT ["/bin/bash"]

CMD ["run"]
