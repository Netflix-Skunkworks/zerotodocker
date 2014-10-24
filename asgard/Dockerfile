FROM netflixoss/tomcat:7
MAINTAINER Netflix Open Source Development <talent@netflix.com>

RUN wget -q https://github.com/Netflix/asgard/releases/download/asgard-1.5/asgard.war &&\
  mkdir ROOT &&\
  cd ROOT &&\
  jar xf ../asgard.war &&\
  cd .. &&\
  mv ROOT /tomcat/webapps/ROOT &&\
  rm asgard.war
  
EXPOSE 8080

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]
