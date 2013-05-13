---
title: "Tent Guide #1: Setting Up a Tent Server"
created_at: 2012-12-9 12:00:00 +0000
kind: article
tags:
  - tent
  - social networking
  - howto
  - decentralization
  - tech
---

This guide will detail how to set up and run your very own Tent v0.2 server on your own hardware. It will cover the proper installation and configuration on either Ubuntu Server 12.04 or an updated copy of Arch Linux. A follow-up post will detail how to use the TentStatus client (or other clients) to interact with your Tent server.

<!-- more -->

**This guide is NOT foolproof by any means and your results may vary based on architecture or the Git commit you are working from.** Remember to visit [tent.io](http://tent.io) or the [GitHub repository](https://github.com/tent/tentd-admin) if you have any questions regarding getting your server up and running. As the software is still very experimental, don't get discouraged if you can't figure things out on your first go. There are a few resources from other experienced users here and there on the web if your Google-fu is strong enough. Also, make sure you replace `$USERNAME`, `$PASSWORD`, and `mydomain.com` with the appropriate values where they come up.


## Install Packages

First things first, you'll want to make sure the following packages are installed:

**Arch:** Install [tentd-admin from the AUR](https://aur.archlinux.org/packages/tentd-admin-git/). It will automatically clone and install the Git repository at `/var/lib/tentd-admin`.
(If you are running Arch, you will need to add `~/.gem/ruby/1.9.1/bin` to your `PATH` environment variable so you can run the gem binaries.)


**Ubuntu:**

~~~
#!bash
sudo apt-get install git ruby1.9.1-full libxml2 libxml2-dev libxslt1-dev build-essential postgresql postgresql-server-dev-all postgresql-client nodejs
sudo gem install bundler
sudo gem install rake
~~~
{:.highlight}


## Setting Up the PostgreSQL Database

Tent uses a PostgreSQL database to store statuses and content. We will add a PostgreSQL database and configure it to accept connections from our Tent server.


**Arch Only:** First we need to initialize the database and start up the PostgreSQL server, since it is not done for us automatically. Run the following commands to do so.

~~~
#!bash
sudo mkdir /var/lib/postgres/data
sudo chown -c postgres:postgres /var/lib/postgres/data
sudo initdb -D '/var/lib/postgres/data'
sudo systemctl start postgresql
sudo systemctl enable postgresql
~~~
{:.highlight}


**Arch and Ubuntu**: We need to configure PostgreSQL's default admin user and assign it a password for security purposes.

~~~
#!bash
sudo -u postgres psql postgres
\password postgres
~~~
{:.highlight}

It will ask you to set a password. Enter \d to exit this prompt when you are done.

Now we will create a username and password with which we will access the server's profile configuration and other tools. This username and password will need to be entered every time you want to pair a new client application with Tent. It's often easiest to make the username the same as what your Linux user is on your server. That way you won't have to change the user via su whenever you need to directly access the database or change its contents.

~~~
#!bash
sudo -u postgres createuser $USERNAME
~~~
{:.highlight}

Next, create a new Tent database and initialize it.

~~~
#!bash
createdb tent_server
~~~
{:.highlight}

Log into PostgreSQL and set the password you want to use when connecting to your database. If your database username created above doesn't match that of your Linux user, you'll need to add "sudo -u $USERNAME" in front of this command.

~~~
#!bash
psql tent_server
tent_server_test=> ALTER ROLE $USERNAME ENCRYPTED PASSWORD '$PASSWORD';
tent_server_test=> \q
~~~
{:.highlight}


## Fetching and Installing the Tent Source

**Ubuntu Only:** We will use Git to install the newest copy of source available for our server. Go to a location on your drive that you want your server to be based on, and that you have write access to.

~~~
#!bash
git clone https://github.com/tent/tentd-admin.git tentd-admin
cd tentd-admin
~~~
{:.highlight}

Now we will install and compile the various services needed to make the Tent server run.

~~~
#!bash
bundle install
~~~
{:.highlight}

You may experience some errors here, but usually they are accompanied by enough information to deduce the source of the problem. As of now this process works with current versions of Ubuntu 12.04, as long as you have followed the steps in this order.


**Arch and Ubuntu**: CD to your install directory, then initialize the database:

~~~
#!bash
DATABASE_URL=postgres://$USERNAME:$PASSWORD@localhost/tent_server bundle exec rake db:migrate
~~~
{:.highlight}

Now we will utter the magic words that bring our server to life (make sure it's all on one line):

~~~
#!bash
DATABASE_URL=postgres://$USERNAME:$PASSWORD@localhost/tent_server ADMIN_USERNAME=$USERNAME ADMIN_PASSWORD=$PASSWORD bundle exec puma -p 3000
~~~
{:.highlight}

Once you've run the above, you should see a confirmation that your server is listening for requests at http://0.0.0.0:3000. Open up a web browser and enter go to http://localhost:3000. If you are on a remote computer, use the server's IP address instead of localhost. If you see "Tent!" then your server is operational.

To set up a quick profile, browse to http://localhost:3000/admin. It will prompt you for the database username and password that we set up earlier. If a screen of checkboxes comes up, click Grant Access to proceed. You will then be greeted with a series of fields that you can fill in to change your name, location, birthdate and other profile-like information.

![](/img/20121209001.png)

Congrats, your server is working!

You will notice that your server suddenly **stops** working if you cancel the Puma command or exit your server's SSH session (provided that's how you're accessing your server). BUT you can run Puma under Screen if you first export your environment variables.

~~~
#!bash
export DATABASE_URL=postgres://$USERNAME:$PASSWORD@localhost/tent_server 
export ADMIN_USERNAME=$USERNAME 
export ADMIN_PASSWORD=$PASSWORD
screen bundle exec puma -p 3000
~~~
{:.highlight}


## Separate Entity and Server Address under Apache

In some cases it may be useful to set up your entity as being a different address than your server. For example, if you would like your Tent entity (handle) to be https://mydomain.com, but you also want your website to be served by this address. So your server would need to be positioned on something like https://tent.mydomain.com. This can be accomplished by adding the following lines into your Apache VirtualHost file(s) for your main page at mydomain.com: 

~~~
#!bash
Header set Link '<https://tent.mydomain.com/profile>; rel="https://tent.io/rels/profile"'
~~~
{:.highlight}

Make sure the Apache mods "headers" and "proxy" are enabled. You will also need to add the `TENT_ENTITY` environment variable to your Puma command, and it should match your desired entity address. You should probably do this before you do anything with your account, like posting or following, as it may create conflicting messages in your followers' streams with two different entities. Reload your Apache configuration and make sure your profile settings are properly set to use the right entity/server addresses, and you're set!


---

The next guide in this series will explain how to use TentStatus with your new Tent server. Stay tuned!
