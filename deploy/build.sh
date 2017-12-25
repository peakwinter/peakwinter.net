#!/usr/bin/env bash
set -e

mkdir _site
docker pull jekyll/jekyll
docker run --rm --volume "$PWD:/srv/jekyll" -it jekyll/jekyll:3.4 jekyll build

if [ ! "env:$TRAVIS_BRANCH" == "env:master" ]; then
    echo "not on master, not pushing"
    exit 0
fi

docker build -t $DOCKER_REPO:latest .

if [ "env:$TRAVIS_BRANCH" == "env:master" ]; then
  docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"
  docker push $DOCKER_REPO:latest
  sudo chown -R travis:travis /home/travis/
fi
