FROM netflixoss-java:7

RUN apt-get update &&\
  apt-get -y install ca-certificates gradle git &&\
  git clone https://github.com/Netflix/karyon.git &&\
  cd karyon &&\
  git checkout tags/1.0.26 &&\
  cd karyon-examples/hello-netflix-oss &&\
  ../../gradlew war
