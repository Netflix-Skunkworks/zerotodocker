FROM netflixoss-tomcat:7

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