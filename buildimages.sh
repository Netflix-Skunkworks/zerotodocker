#!/bin/sh

cd java/7
docker build -t netflixoss-java:7 .
cd ../..

cd tomcat/7
docker build -t netflixoss-tomcat:7 .
cd ../..



cd asgard
docker build -t netflixoss-asgard:1.5 .
cd ..

cd eureka
docker build -t netflixoss-eureka:1.1.142 .
cd ..

cd exhibitor-zookeeper
docker build -t netflixoss-exhibitor:1.5.2 .
cd ..

cd zuul
docker build -t netflixoss-zuul:1.0.28 .
cd ..

cd hello-netflix-oss-buildwar
docker build -t hello-netflix-oss-buildwar:temp .
rm -rf output
mkdir output
THECMD="cp /karyon/karyon-examples/hello-netflix-oss/build/libs/hello-netflix-oss-1.0.26.war /output/."
docker run -v ${PWD}/output:/output hello-netflix-oss-buildwar:temp $THECMD
cp output/hello-netflix-oss-1.0.26.war ../hello-netflix-oss/.
cd ..

cd hello-netflix-oss
docker build -t netflixoss-hello-netflix-oss:1.0.26 .
cd ..

# TODO Cassandra/Priam

# TODO Chaos Monkey