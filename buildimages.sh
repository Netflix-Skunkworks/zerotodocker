#!/bin/sh

# Copyright 2014 Netflix, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## BASE IMAGES ##

cd java/7
docker build -t netflixoss/java:7 .
cd ../..

cd java/8
docker build -t netflixoss/java:8 .
cd ../..

cd tomcat/7
docker build -t netflixoss/tomcat:7 .
cd ../..

## PLATFORM ##

cd asgard
docker build -t netflixoss/asgard:1.5 .
cd ..

cd eureka
cd 1.1.142
docker build -t netflixoss/eureka:1.1.142 .
cd ..
cd 1.1.147
docker build -t netflixoss/eureka:1.1.147 .
cd ..
cd ..

cd exhibitor-zookeeper
docker build -t netflixoss/exhibitor:1.5.2 .
cd ..

cd zuul
docker build -t netflixoss/zuul:1.0.28 .
cd ..

cd hello-netflix-oss
docker build -t netflixoss/hello-netflix-oss:1.0.27 .
cd ..

## SECURITY MONKEY ##

cd security_monkey/security_monkey-api
docker build -t netflixoss/security_monkey-api:0.2.0 .
cd ../..

cd security_monkey/security_monkey-apiinit
docker build -t netflixoss/security_monkey-apiinit:0.2.0 .
cd ../..

cd security_monkey/security_monkey-nginx
docker build -t netflixoss/security_monkey-nginx:0.2.0 .
cd ../..

cd security_monkey/security_monkey-scheduler
docker build -t netflixoss/security_monkey-scheduler:0.2.0 .
cd ../..

## SKETCHY ##

cd sketchy/sketchy_api
docker build -t netflixoss/sketchy-api:1.0.0 .
cd ../..

cd sketchy/sketchy_nginx
docker build -t netflixoss/sketchy-nginx:1.0.0 .
cd ../..

## EDDA ##
cd edda/2.1
docker build -t netflixoss/edda:2.1 .
cd ../..

