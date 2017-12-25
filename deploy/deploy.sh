#!/usr/bin/env bash
set -e

if [ ! "env:$TRAVIS_BRANCH" == "env:master" ]; then
    echo not on master, not deploying
    exit 0
fi

echo "on master ✓"

if [ -z "$server" ]; then
    echo "server" variable not set
    exit 1
fi
echo "deploying to: $server ✓"

echo "decrypting ssh key..."
openssl aes-256-cbc -K $encrypted_addab9536e63_key -iv $encrypted_addab9536e63_iv -in deploy/key.enc -out deploy/key -d
chmod 400 deploy/key

echo "setting StrictHostKeyChecking for all domains..."
printf "Host *\n    StrictHostKeyChecking no\n" > ~/.ssh/config
chmod 400 ~/.ssh/config

echo "copying site to $server..."
scp -i deploy/key docker-compose.yml deploy@$server:"$deploy_to"
ssh -i deploy/key deploy@$server "cd \"$deploy_to\"; docker stack deploy -c docker-compose.yml $project"
rm -f deploy/key

echo "deployment ✓"
