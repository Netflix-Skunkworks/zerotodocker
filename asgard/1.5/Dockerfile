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
