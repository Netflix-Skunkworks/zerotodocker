FROM netflixoss/tomcat:7
MAINTAINER John Jelinek IV <john@johnjelinek.com>

ENV SIMIANARMY_VERSION 2.5-SNAPSHOT

RUN \
  apt-get update &&\
  apt-get install -y git &&\
  git clone git://github.com/Netflix/SimianArmy.git &&\
  cd SimianArmy/ &&\
  ./gradlew build &&\
  mkdir /tomcat/webapps/ROOT &&\
  cd /tomcat/webapps/ROOT &&\
  jar xf /SimianArmy/build/libs/simianarmy-"$SIMIANARMY_VERSION".war &&\
  rm -fr /SimianArmy

# Cleanup
RUN \
  apt-get clean && \
  rm -fr /var/lib/apt/lists/* && \
  rm -fr /tmp/*

EXPOSE 8080

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]
