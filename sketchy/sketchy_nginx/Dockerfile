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

FROM nginx:1.7.7
MAINTAINER Netflix Open Source Development <talent@netflix.com>

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log &&\
  ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 443

ADD sketchy.conf /etc/nginx/sites-available/sketchy.conf
COPY nginx.conf /etc/nginx/nginx.conf
ADD server.crt /etc/ssl/certs/server.crt
ADD server.key /etc/ssl/private/server.key

RUN /bin/mkdir -p /etc/nginx/sites-enabled/ &&\
  ln -s /etc/nginx/sites-available/sketchy.conf /etc/nginx/sites-enabled/sketchy.conf

ENTRYPOINT ["nginx", "-g", "daemon off;"]
