#!/bin/bash

echo '>>> Changing into working directory'
cd /usr/local/src/acereport

echo '>>> Building new docker image (acereport)'
docker build -f production.Dockerfile -t acereport .

echo '>>> Stopping existing container (acereport_container)'
docker stop acereport_container || true

echo '>>> Starting new container (acereport_container)'
docker run --rm -d --name acereport_container acereport
sleep 5

echo '>>> Cleaning up images'
docker images | grep "^<none>" | head -n 1 | awk 'BEGIN { FS = "[ \t]+" } { print $3 }'  | while read -r id ; do
  docker rmi $id
done

echo '>>> Deployment complete'
docker ps -a | grep "acereport"