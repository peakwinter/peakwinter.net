---
template: post
slug: modern-devops-django
title: "Modern DevOps with Django"
image: /assets/images/20180122001.jpg
summary: Setting up a modern development, testing and deployment system for a Django application, using Docker and Gitlab CI.
tags:
  - howto
  - technology
  - development
  - django
  - python
  - docker
  - devops
  - gitlab ci
  - continuous delivery
  - continuous integration
---

There are as many different ways of deploying a Django application as there are opinions about the Python 2 vs. 3 schism. That is to say, there are a lot! Whether you go the old school route with FTP, use good-old SCP, or something a bit more contemporary like Fabric or Ansible, the most important part of your deployment pipeline is that it works well for you without any friction.

Nowadays teams and individuals are demanding more flexibility and speed when it comes to their environments and deployments, and all sorts of applications can benefit from the new developments the past few years have brought to these domains.

The purpose of this post is to set out what I believe is a "modern" DevOps setup for a Django application, using Docker and Gitlab CI. I will walk you what I think it means to have a "modern" DevOps setup in the first place, the reasoning behind these technical choices, and a hop through the different configuration files necessary to get this sort of environment set up for yourself.

Let's get started!

### The Idea

The primary objectives for the DevOps stack of our application are as follows:

* **Allow for continuous integration.** The biggest benefit in my opinion for setting up a [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration) (CI) pipeline for your project is *clarity*. The information that a CI pipeline can provide when properly integrated with external tools for measuring test coverage and code smells (code quality) can be very important for knowing where to devote your attention and resources to make things better.
* **Allow for continuous delivery.** An application that is set up to be [continuously delivered](https://en.wikipedia.org/wiki/Continuous_delivery) will often involve far less stress around the time of major releases, fewer bugs that make it to production (and the ones that do are fixed much more quickly), and easier rollout of things like feature flags and A/B testing. Ultimately, it's a no-brainer switch that can save you time and money.
* **Simplify our hosting system.** Let's be honest - we have far more fun with the *Dev* half of *DevOps* than the *Ops* half. Servers can be a pain to manage - there's package dependencies to contend with, differences in distributions and versions, differences between providers, breaking changes that are difficult to undo... This is why it's important with a DevOps approach to reduce your application's impact on its server environment as much as possible. Using things like containers or virtual machines for your deployments can make a major impact here, because your operating environment is treated as if it was the same as your application - undergoing the same tests and idempotent build processes.

### The Stack

Our setup for this Django app will include several components. First, we will be deploying our Django application using a **[Docker container](https://docs.docker.com/compose/django/)**. Docker allows us to easily create clean, pre-installed images of our application in an isolated state, like a binary application build, rather than having to worry about virtual environments and system packages of whatever server we are deploying to. This build can then be tested and deployed as if it was an isolated artifact in and of itself. Our container can be grouped with other dependent services (databases, memory caches, and so on) together in a `docker-compose.yml` file. Using an advanced hosting mechanism like [Docker Swarm](/blog/swarm-cloud) or [Kubernetes](https://kubernetes.io), we can then deploy our entire application as a "stack" with the push of a button.

This "push of a button" occurs inside the next component of our stack, [Gitlab CI](https://about.gitlab.com/features/gitlab-ci-cd/). An integrated, job-based testing and deployment pipeline system, Gitlab CI is perhaps the best tool available today for quickly and easily building and deploying your Docker-based applications. In our specific setup, on each push:

* to the `develop` branch, commits and merges will build the app and run the test suite
* to the `master` branch, commits and merges will build the app, run the test suite and deploy to staging if successful. Tagged commits pushed to `master` will do the same thing except they will be pushed to production instead.

The application builds as a Docker container, and these containers are stored using the [Gitlab Container Registry](https://docs.gitlab.com/ce/user/project/container_registry.html) - an extremely handy tool that turns your Gitlab instance into a full-featured Docker registry (like [hub.docker.com](https://hub.docker.com)) - pretty cool! In my particular setup, containers are stored with the registry with their branch name tagged. That way, I can keep each version of my application and each branch separate, for re-downloading and testing later if need be.

### The Configuration

*(I've set up a [Github repository](https://github.com/peakwinter/modern-devops-django-sample) where you can check out a full version of these configuration files and more, check it out!)*

#### Dockerfile

First things first is our [Dockerfile](https://docs.docker.com/engine/reference/builder/). This is the configuration that takes a base image (in our case Python 3.6 installed on a thin copy of Alpine Linux) and installs everything our application needs to run, including our Python dependencies. It also sets a default command to use - this is the command that will be executed each time our container starts up in production. We want it to check for any pending migrations, run them, then start up our uWSGI server to make our application available to the Internet. It's safe to do this because if any migrations failed after our automatic deployments to staging, we would be able to recover from that and make the necessary changes before we tag a release and deploy to production.

This Dockerfile example builds a container with necessary dependencies for things like image uploads as well as connections to a PostgreSQL database.

```dockerfile
FROM python:3-alpine3.6

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache linux-headers bash gcc \
    musl-dev libjpeg-turbo-dev libpng libpq \
    postgresql-dev uwsgi uwsgi-python3 git \
    zlib-dev libmagic

WORKDIR /site
COPY ./ /site
RUN pip install -U -r /site/requirements.txt
CMD python manage.py migrate && uwsgi --ini=/site/uwsgi.ini
```

#### Docker Compose configuration

We can now build our application with `docker build -t myapp .` and run it with `docker run -it myapp`. But in the case of our development environment, we are going to use Docker Compose in practice. The Docker Compose configuration below is sufficient for our development environment, and will serve as a base for our configurations in staging and production, which can include things like Celery workers and monitoring services.

```yaml
version: '3'

services:
  app:
    build: ./
    command: bash -c "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"
    volumes:
      - ./:/site:rw
    depends_on:
      - postgresql
      - redis
    environment:
      DJANGO_SETTINGS_MODULE: myapp.settings.dev
    ports:
      - "8000:8000"

  postgresql:
    restart: always
    image: postgres:10-alpine
    volumes:
      - ./.dbdata:/var/lib/postgresql:rw
    environment:
      POSTGRES_USER: myapp
      POSTGRES_PASSWORD: myapp
      POSTGRES_DB: myapp

  redis:
    restart: always
    image: redis:latest
```

This is a pretty basic configuration - all we are doing is setting a startup command for our app (similar to the entrypoint in our Docker container, except this time we are going to run Django's internal dev server instead) and initializing PostgreSQL and Redis containers that will be linked with it. It's important to note that `volumes` line in our app service &mdash; this is going to bind the current directory of source code on our host machine to the installation folder inside the container. That way we can make changes to the code locally and still use the automatic reloading feature of the Django dev server.

At this point, all we need to do is `docker-compose up`, and our Django application will be listening on port 8000, just as if we were running it from a virtualenv locally. This configuration is perfectly suitable for **developer environments** &mdash; all anyone needs to do to get started using the exact same environment as you is to clone the Git repository and run `docker-compose up`!

#### Testing and Production

For testing your application, whether that's on your local machine or via Gitlab CI, I've found it's helpful to create a clone of this `docker-compose.yml` configuration and customize the command directive to instead run whatever starts your test suite. In my case, I use the Python `coverage` library, so I have a second file called `docker-compose.test.yml` which is exactly the same as the first, save for the command directive has been changed to:

```yaml
command: bash -c "coverage run --source='.' manage.py test myapp && coverage report"
```

Then, I run my test suite locally with `docker-compose -p test -f docker-compose.test.yml up`.

For production and staging environments, I do the same thing &mdash; duplicate the file with the few changes I need to make for the environment in particular. In this case, for production, I don't want to provide a build path &mdash; I want to tell Docker that it needs to take my application from the container registry each time it starts up. To do so, remove the `build` directive and add an `image` one like so:

```yaml
image: registry.gitlab.com/pathto/myapp:prod
```

#### Continuous Integration and Delivery

Now we get to the fun part!

Since we are working with Gitlab CI, we are going to need to create a `.gitlab-ci.yml` file, which contains within it all of the instructions that Gitlab needs to properly set up our testing and deployment pipeline. This guide assumes you have CI enabled on your Gitlab instance of choice, and have set up Shell and Docker runners on an external server. Doing so is beyond the scope of this guide, but there are [plenty of walkthroughs](https://about.gitlab.com/2016/04/19/how-to-set-up-gitlab-runner-on-digitalocean/) online if you need help!

I'm going to walk through this configuration step-by-step, so we can get a better grasp of what's going on.

```yaml
stages:
  - build
  - test
  - release
  - deploy

variables:
  CONTAINER_IMAGE: registry.gitlab.com/pathto/myapp
  CONTAINER_TEST_IMAGE: $CONTAINER_IMAGE:$CI_BUILD_REF_NAME
  DEPLOY_SERVER_URL: myserver.example.com
  DEPLOY_PATH: /var/data/myapp
```

Each job we set up in our Gitlab CI pipeline will correspond to one of these stages, so we can control what jobs get executed concurrently and at which point the pipeline stops if it encounters a problem. We also set up a few handy variables here that we will reference later.

* `CONTAINER_IMAGE`: the path to our repository on the Gitlab Container Registry
* `CONTAINER_TEST_IMAGE`: the name of the image and tag for the branch we are running the pipeline on
* `DEPLOY_SERVER_URL`: the name of one of our Docker Swarm master nodes that we will connect to via SSH.
* `DEPLOY_PATH`: the path on the server to deploy our Docker configurations to.

Now, we start our pipeline with the **build** step:

```yaml
build:
  stage: build
  tags:
    - shell
  script:
    - docker login -u gitlab-ci-token -p $CI_JOB_TOKEN registry.gitlab.com
    - docker build -t $CONTAINER_TEST_IMAGE .
    - docker push $CONTAINER_TEST_IMAGE
```

We choose a Shell executor for Gitlab CI because that is the quickest and easiest way to build and work with Docker containers from the outside. This may not be a suitable option for everyone, however &mdash; make sure you read up on the Gitlab CI configuration when you set up your runner infrastructure.

Here we execute three commands: the first will login to the Gitlab Container Registry with a custom token (you'll see this command a lot), the second builds our container and tags it with the current branch name, and the third pushes this tagged container to our registry. At this point, we can now download a copy of our application at the state of this branch using this tag.

Now we get into the **testing** jobs:

```yaml
codequality:
  stage: test
  tags:
    - shell
  script:
    - docker login -u gitlab-ci-token -p $CI_JOB_TOKEN registry.gitlab.com
    - docker pull codeclimate/codeclimate
    - docker run --env CODECLIMATE_CODE="$PWD" --volume "$PWD":/code --volume /var/run/docker.sock:/var/run/docker.sock --volume /tmp/cc:/tmp/cc codeclimate/codeclimate analyze -f json > codeclimate.json
  artifacts:
    paths: [codeclimate.json]

test:
  stage: test
  tags:
    - shell
  script:
    - docker login -u gitlab-ci-token -p $CI_JOB_TOKEN registry.gitlab.com
    - docker pull $CONTAINER_TEST_IMAGE
    - docker-compose -f docker/compose.ci.yml -p ci up --abort-on-container-exit
  coverage: '/TOTAL.*?(\d{1,2}.\d+%)/'
```

Here we have two jobs for testing. One is for analyzing code smells and style, using the Code Climate analyzer. This will run a variety of checks including for cyclomatic complexity and PEP 8 compatibility. The other is for running the unit test suite that comes with our Django application. If any tests fail, the job will fail and we will be able to see a readout of what went wrong on our Gitlab site.

Each time we perform an operation with our container, we pull the container at the state it was during our build step, using the tag name assigned to it. This way we are always testing the container we have already built, rather than the application code alone.

Since these two jobs are in the same stage, they run concurrently, and the pipeline will not advance until the next stage unless they both pass.

```yaml
release_stg:
  stage: release
  tags:
    - shell
  only:
    - master
  script:
    - docker login -u gitlab-ci-token -p $CI_JOB_TOKEN registry.gitlab.com
    - docker tag $CONTAINER_TEST_IMAGE $CONTAINER_IMAGE:staging
    - docker push $CONTAINER_IMAGE:staging
```

If we made it past our wonderful testing system, we get to the point where we stamp our container with a big "ACCEPTED" stamp, and **release** it to production (or staging, as the case may be). This job merely takes the passing container, tags it with either "prod" or "staging" so that we can match the state of our production or staging services at any given time, then pushes that tag to our container registry.

```yaml
deploy_stg:
  stage: deploy
  tags:
    - docker
  only:
    - master
  environment:
    name: staging
    url: https://staging.example.com
  before_script:
    - 'which ssh-agent || ( apt-get update -y && apt-get install openssh-client -y )'
    - eval $(ssh-agent -s)
    - echo "$DEPLOY_KEY" | ssh-add -
    - mkdir -p ~/.ssh
    - '[[ -f /.dockerenv ]] && echo -e "Host *\n\tStrictHostKeyChecking no\n\n" > ~/.ssh/config'
  script:
    - scp docker-compose.staging.yml deploy@$DEPLOY_SERVER_URL:$DEPLOY_PATH/staging/docker-compose.yml
    - ssh deploy@$DEPLOY_SERVER_URL "cd $DEPLOY_PATH/staging && docker stack deploy -c docker-compose.yml --with-registry-auth myapp_staging"
```

Now the *really* fun part! **Deploying** our application can be done in a variety of ways. In my case, it is done by SSHing to a master in my [Docker Swarm](/blog/swarm-cloud), copying over the Compose configurations, then deploying them as a [Stack](https://docs.docker.com/docker-cloud/apps/stacks/). The same idea can also be used for a deployment to any Docker server &mdash; just replace the `docker stack deploy` with a `docker-compose up` and the same basic concept holds true.

In order to properly authenticate with our server, Gitlab CI needs to know where to find an SSH private key. You can set this up as a secret variable within your Gitlab CI repository itself. Then, as we see in the `before_script` section, we do some magic that tells Gitlab to take the value of that secret variable and to insert it into our container as an SSH private key file.

Our `script` section is very minimal, since all we are doing is copying over our Docker Compose configuration file, then telling the Docker daemon on our server to run it. If you are using Docker Swarm and the `docker stack deploy` command, this one command will intelligently restart different components of the stack if their configurations have changed or if there are newer versions of their images available on our container registry (which is always the case here, since we just submitted a new release to it!).

### Conclusion

With that, we've set up a DevOps stack for our Django app that assures a fast, capable and continuous build system, that is easily testable and requires very little maintenance for system administrators.

If you'd like to check at the full list of configuration files, I've set up a [Github repository](https://github.com/peakwinter/modern-devops-django-sample) where you can see them, feel free to take any snippets you need. And if you have any questions or comments be sure to drop me a line!