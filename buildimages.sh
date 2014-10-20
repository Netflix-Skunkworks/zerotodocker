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
docker build -t netflixoss-zuul:1.0.24 .
cd ..

# TODO Cassandra/Priam

# TODO Chaos Monkey

# TODO Sample App