#!/bin/sh
docker ps -q | xargs docker inspect --format '{{ .NetworkSettings.IPAddress }}  {{ .Name }} {{ .Config.Image }} {{ .State.Running }} {{ .Id }}'
