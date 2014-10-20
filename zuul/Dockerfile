FROM netflixoss-tomcat:7

RUN cd /tomcat/webapps &&\
  mkdir ROOT &&\
  cd ROOT &&\
  wget -q http://repo1.maven.org/maven2/com/netflix/zuul/zuul-netflix-webapp/1.0.24/zuul-netflix-webapp-1.0.24.war &&\
  jar xf zuul-netflix-webapp-1.0.24.war &&\
  rm zuul-netflix-webapp-1.0.24.war

ADD config.properties /tomcat/webapps/ROOT/WEB-INF/classes/config.properties
ADD zuul-test.properties /tomcat/webapps/ROOT/WEB-INF/classes/zuul-test.properties
  
EXPOSE 8080

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]