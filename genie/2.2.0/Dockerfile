# Copyright 2015 Netflix, Inc.
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

# Properties to set
ENV CATALINA_OPTS="-Dspring.profiles.active=prod -Darchaius.deployment.applicationId=genie -Darchaius.deployment.environment=prod"

# Lots of commands to configure the Genie system grouped together to save on filesystem layers in Docker
# (Lines 28-33) Download and extract the Genie WAR file
# (34) Create the Genie Jobs directory where job results will be stored and DB connection info
# (35-37) Enable listings in Tomcat and configure it with listings.xsl
# (38-39) Configure the database connection to use mysql-genie Docker link as hostname and the correct password
# (40-48) Modify default properties to map to the Docker image locations and settings
# (49-58) Download and configure all the Genie scripts that are used to run jobs
RUN wget -q -P /tomcat/webapps 'http://jcenter.bintray.com/com/netflix/genie/genie-web/2.2.1/genie-web-2.2.1.war' &&\
  mkdir /tomcat/webapps/ROOT &&\
  cd /tomcat/webapps/ROOT &&\
  jar xf ../genie-web-2.2.0.war &&\
  cd .. &&\
  rm genie-web-2.2.0.war &&\
  mkdir /tomcat/webapps/genie-jobs &&\
  wget -q -P /tomcat/conf 'https://raw.githubusercontent.com/Netflix/genie/2.2.1/root/apps/tomcat/conf/listings.xsl' &&\
  sed -i '111s/false/true/' /tomcat/conf/web.xml &&\
  sed -i '113i\ \ \ \ \ \ \ \ <init-param>\n\ \ \ \ \ \ \ \ \ \ \ \ <param-name>globalXsltFile<\/param-name>\n\ \ \ \ \ \ \ \ \ \ \ \ <param-value>\/tomcat\/conf\/listings.xsl<\/param-value>\n\ \ \ \ \ \ \ \ <\/init-param>' /tomcat/conf/web.xml &&\
  sed -i '69s/127.0.0.1/mysql-genie/' /tomcat/webapps/ROOT/WEB-INF/classes/genie-jpa.xml &&\
  sed -i '71s/value=""/value="genie"/' /tomcat/webapps/ROOT/WEB-INF/classes/genie-jpa.xml &&\
  sed -i '23s/\/usr\/lib\/jvm\/java-1.7.0-sunjdk.x86_64/\/usr\/lib\/jvm\/java-7-oracle/' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i '26s/\/apps\/hadoop\/current/\/apps\/hadoop\/2.6.0/' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i '27s/com.netflix.genie.server.hadoop.2.4.0.home=\/apps\/hadoop\/2.4.0/com.netflix.genie.server.hadoop.2.6.0.home=\/apps\/hadoop\/2.6.0/' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i '83s/\/mnt\/tomcat\/genie-jobs/\/tomcat\/webapps\/genie-jobs/' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i '98,105d' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i '99icom.netflix.genie.server.job.manager.yarn.command.cp=\/apps\/hadoop\/2.6.0\/bin\/hadoop fs -cp -f' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i '101,108d' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  sed -i '101icom.netflix.genie.server.job.manager.yarn.command.mkdir=\/apps\/hadoop\/2.6.0\/bin\/hadoop fs -mkdir' /tomcat/webapps/ROOT/WEB-INF/classes/genie.properties &&\
  mkdir -p /apps/genie/bin &&\
  wget -q -P /apps/genie/bin 'https://raw.githubusercontent.com/Netflix/genie/2.2.1/root/apps/genie/bin/jobkill.sh' &&\
  chmod 755 /apps/genie/bin/jobkill.sh &&\
  wget -q -P /apps/genie/bin 'https://raw.githubusercontent.com/Netflix/genie/2.2.1/root/apps/genie/bin/joblauncher.sh' &&\
  chmod 755 /apps/genie/bin/joblauncher.sh &&\
  sed -i '233s/conf/etc\/hadoop/' /apps/genie/bin/joblauncher.sh &&\
  wget -q -P /apps/genie/bin 'https://raw.githubusercontent.com/Netflix/genie/2.2.1/root/apps/genie/bin/localCleanup.py' &&\
  chmod 755 /apps/genie/bin/localCleanup.py &&\
  wget -q -P /apps/genie/bin 'https://raw.githubusercontent.com/Netflix/genie/2.2.1/root/apps/genie/bin/timeout3' &&\
  chmod 755 /apps/genie/bin/timeout3

# Below here optional to run Genie and can be different for different deployments

# Download and configure hadoop client
RUN mkdir -p /apps/hadoop/2.6.0 &&\
  cd /apps/hadoop/2.6.0 &&\
  wget -q -P /apps/hadoop/2.6.0 'http://apache.cs.utah.edu/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz' &&\
  tar xf hadoop-2.6.0.tar.gz &&\
  rm hadoop-2.6.0.tar.gz &&\
  chown root:root -R hadoop-2.6.0 &&\
  mv hadoop-2.6.0/* . &&\
  rm -rf hadoop-2.6.0

ENV HADOOP_HOME=/apps/hadoop/2.6.0
ENV HADOOP_PREFIX=$HADOOP_HOME
ENV PATH=$HADOOP_HOME/bin:$PATH

# This is not needed to get Genie working as the scripts loaded into conf below can be copied at runtime
# I'm just adding them here so that the hadoop and pig commands can connect to the cluster from Genie node by default
# in case someone wants to mess around with them as a client
ADD hadoop/2.6.0/conf/*.xml $HADOOP_HOME/etc/hadoop/

# Download and configure pig client
RUN mkdir -p /apps/pig/0.14.0 &&\
  cd /apps/pig/0.14.0 &&\
  wget -q -P /apps/pig/0.14.0 'http://apache.cs.utah.edu/pig/pig-0.14.0/pig-0.14.0.tar.gz' &&\
  tar xf pig-0.14.0.tar.gz &&\
  rm pig-0.14.0.tar.gz &&\
  chown root:root -R pig-0.14.0 &&\
  mv pig-0.14.0/* . &&\
  rm -rf pig-0.14.0

ENV PIG_HOME=/apps/pig/0.14.0
ENV PATH=$PIG_HOME/bin:$PATH

# Install some packages that will be used for the example
RUN apt-get update &&\
  DEBIAN_FRONTEND=noninteractive apt-get -y install python python-pip vim &&\
  python -m pip install --no-input --upgrade --force pip &&\
  pip install nflx-genie-client==2.2.0

# Put the example scripts onto the image if people want to use them
ADD hadoop/2.6.0/conf/*.xml /apps/genie/hadoop/2.6.0/conf/
ADD pig/0.14.0/tutorial/* /apps/genie/pig/0.14.0/tutorial/
ADD example/*.py /apps/genie/example/

EXPOSE 8080

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]
