FROM netflixoss-tomcat:7

ADD hello-netflix-oss-1.0.26.war /hello-netflix-oss-1.0.26.war

RUN cd /tomcat/webapps &&\
  mkdir ROOT &&\
  cd ROOT &&\
  cp /hello-netflix-oss-1.0.26.war . &&\
  jar xf hello-netflix-oss-1.0.26.war &&\
  rm hello-netflix-oss-1.0.26.war &&\
  rm WEB-INF/classes/hello-netflix-oss-dev.properties &&\
  rm WEB-INF/classes/hello-netflix-oss.properties &&\
  rm WEB-INF/classes/eureka-client.properties

ADD config.properties /tomcat/webapps/ROOT/WEB-INF/classes/config.properties
ADD hello-netflix-oss.properties /tomcat/webapps/ROOT/WEB-INF/classes/hello-netflix-oss.properties
ADD hello-netflix-oss-test.properties /tomcat/webapps/ROOT/WEB-INF/classes/hello-netflix-oss-test.properties
  
EXPOSE 8080 8077

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]