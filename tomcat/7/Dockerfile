FROM netflixoss-java:7

RUN apt-get update &&\
  apt-get -y install ca-certificates &&\
  wget -q https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.56/bin/apache-tomcat-7.0.56.tar.gz.md5 &&\
  wget -q http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.56/bin/apache-tomcat-7.0.56.tar.gz &&\
  md5sum -c apache-tomcat-7.0.56.tar.gz.md5 &&\
  tar xzf apache-tomcat-7.0.56.tar.gz &&\
  rm /apache-tomcat-*.tar.gz* &&\
  mv /apache-tomcat-7.0.56 /tomcat &&\
  cd /tomcat/webapps &&\
  rm -Rf ROOT docs examples
  
EXPOSE 8080

ENTRYPOINT ["/tomcat/bin/catalina.sh"]

CMD ["run"]
