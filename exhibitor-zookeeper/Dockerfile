FROM netflixoss/java:7
MAINTAINER Netflix Open Source Development <talent@netflix.com>

RUN apt-get update &&\
  apt-get -y install ca-certificates &&\
  wget -q http://archive.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz.md5 &&\
  wget -q http://archive.apache.org/dist/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz &&\
  md5sum -c zookeeper-3.4.6.tar.gz.md5 &&\
  tar xzf zookeeper-3.4.6.tar.gz &&\
  rm /zookeeper-3.4.6.tar.gz* &&\
  mv /zookeeper-3.4.6 /zookeeper
  
RUN apt-get -y install maven &&\
  mkdir /exhibitor &&\
  cd /exhibitor

ADD pom.xml /exhibitor/pom.xml
  
RUN cd /exhibitor &&\
  mvn assembly:single &&\
  mv target/exhibitor-1.0-jar-with-dependencies.jar . &&\
  rm -rf /exhibitor/target &&\
  rm /exhibitor/pom.xml
  
ADD exhibitor.properties /exhibitor/exhibitor.properties

EXPOSE 2181 2888 3888 8080

WORKDIR /exhibitor

ENTRYPOINT ["java", "-jar", "exhibitor-1.0-jar-with-dependencies.jar", "-c", "file"]
