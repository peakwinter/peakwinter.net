---
layout: post
title: "Alternatives to US Clouds for Developers"
image: /assets/images/20170603001.jpg
description: For the safety of your bits and bytes, it's time to start looking elsewhere.
tags:
- privacy
- technology
- politics
---

Executive orders by the Trump administration [have seriously jeopardized](https://techcrunch.com/2017/01/26/trump-order-strips-privacy-rights-from-non-u-s-citizens-could-nix-eu-us-data-flows/) the prospect of non-US citizens having any privacy rights over their data stored in that country &mdash; a development that is [seriously jeopardizing](https://www.euractiv.com/section/data-protection/news/meps-want-commission-to-toughen-up-privacy-shield-under-trump/) many international privacy relationships, including the European Union's "Privacy Shield" accord. This comes during a veritable tidal wave of bad news regarding tech and privacy policy in the United States. In only the past few months, we've heard that protections against [ISP data sharing have been nixed](http://money.cnn.com/2017/04/03/technology/internet-privacy-law-trump/index.html), that net neutrality is [to be a thing of the past](http://variety.com/2017/biz/news/donald-trump-net-neutrality-reversal-1202019819/), and that new visa applicants may have to [provide access to their social media](http://www.bbc.com/news/technology-40132506) accounts.

There are potentially very dark days ahead for tech users and responsible companies that are concerned with privacy issues. Many developers and users may want to start thinking outside the box when it comes to their next service subscription or startup idea &mdash; or, rather, outside the reach of Uncle Sam.

So, without further ado, here's a list of companies and services you should check out if you're looking to move away from the Stars and Stripes for your next project. *(Note: these are all services I've used and enjoyed in the past few years, and none of these links are referral links!)*


### Exoscale

{: .pull-right}
![](/assets/images/20170603002.jpg)

[Exoscale](https://www.exoscale.ch) is a relatively new company based in Switzerland which offers several cloud services geared towards developers. What I like the most about them is that they seem to be trying to create a European version of Digital Ocean: providing similar services at similar prices, but with the added benefit of being based under Swiss privacy legislation, which is for the most part compatible with that of the European Union. And best of all, they now even compete favourably with DO in terms of pricing (which hasn't always been the case). Case in point: you can get a 4 GB virtual server with 2 CPU cores and 100 GB of SSD storage for $42 per month, whereas Digital Ocean's equivalent offering only gives 60 GB. You can also choose the size of your storage and are not locked in to a specific limit based on the server you choose. Pretty cool.

Exoscale doesn't just offer virtual servers: they have an [object storage service](https://www.exoscale.ch/object-storage/) that uses the same API as Amazon's S3, as well as a [GPU-based compute](https://www.exoscale.ch/gpu/) service, [anycast DNS hosting](https://www.exoscale.ch/dns/) (think Route53) and a nifty [status page service](https://www.exoscale.ch/runstatus/).

**Pros:**

* Competitive pricing for what you get
* Bills in euros, US dollars or Swiss francs
* Swiss security (complies with EU data protection rules) and quality

**Cons:**

* Younger service less established in the market
* Watch out for bandwidth billing


### Scaleway / Online

{: .pull-right}
![](/assets/images/20170603003.jpg)

Online was founded in 1999 and is a subsidiary of a French conglomerate named Iliad which, in addition to specializing in all things "datacenter", owns a popular telecom company called Free. All of that to say that Online isn't a startup and doesn't seem to be going anywhere anytime soon.

The [Online.net](https://www.online.net/) brand is primarily oriented towards the dedicated server market and, much like its rival OVH, has dozens of different hardware profiles to choose from based on your individual needs. Beyond this, it has recently launched two new innovative services. The first is called [**C14**](https://www.online.net/en/c14), an object storage service similar in nature to Amazon Glacier, in that it offers super-cheap prices for storage (only ~$0.0022 per GB/month) if you are willing to put up with a transaction cost ($0.011 per GB) and retrieval time of up to a couple hours a pop. The second is a database-as-a-service (DBaaS) platform called [**ODS**](https://www.online.net/en/ods), which offers a no-nonsense monthly fee and supports the most popular database systems in use today: MySQL, PostgreSQL, MariaDB and MongoDB.

Online has a popular subsidiary called [Scaleway](https://www.scaleway.com) which caters to the cloud-based compute and embedded markets. They've brought super-cheap virtual private servers (VPS) and dependable ARM-based dedicated servers to market, with a resolutely developer-friendly approach. "Spin up" your services using a Dockerfile-like configuration and they will run on your Scaleway server just like if it was a container. I've been a Scaleway customer for awhile now and, while the software and billing systems can be a bit rough around the edges, it's a very cool platform with a bright future if they can keep expanding to meet the offerings of other providers.

**Pros:**

* Cheap, cheap, cheap!
* Lots of service options for computing power
* A company that is constantly innovating with new offerings

**Cons:**

* Only bills in euros
* Customer service is occasionally inflexible or slow to respond
* Scaleway's object storage service languishing in Beta


### OVH

{: .pull-right}
![](/assets/images/20170603004.jpg)

[OVH](https://www.ovh.com) is one of the largest hosting companies in the world, so it's surprising how many people are not yet familiar with its offerings. They have different options depending on which market you are in, but the lion's share of their business has been built on a model of mass-produced dedicated servers in cavernous datacenters. OVH has a dizzying array of different combinations of dedicated servers depending on your exact use case. If you're willing to go DIY, you can use their servers to build your own cloud using solutions like OpenStack and the resulting prices are often much cheaper than what you are charged at an existing provider.

Beyond dedicated servers, they have a few solid (and very cheap) options for VPSes, which I use currently for my projects and am very happy with. They are a great option for object storage using OpenStack Swift, and extremely cheap at that &mdash; only $0.0112 per GB/month and $0.011 per GB for outgoing traffic.

OVH has many subsidiaries targeting different segments of the market: [Kimsufi](https://www.kimsufi.com/en/) for the budget-conscious customer with ephemeral needs, [RunAbove](https://www.runabove.com/) for the early-adopting developer looking to experiment with new technologies, or [SoYouStart](https://www.soyoustart.com/ca/en/) for newly-minted startups looking for the cheapest and fastest way to launch their MVP.

**Pros:**

* Dirt cheap and bills in many local currencies
* Datacenters in Canada and Europe, and constantly expanding
* Comprehensive developer API

**Cons:**

* Documentation is often disparate and of poor quality
* Admin portals seriously need a facelift
* Service renewals are manual


### Gandi

{: .pull-right}
![](/assets/images/20170603005.jpg)

[Gandi](https://www.gandi.net/en) is on this list because I've been one of their biggest fans for many years now. Their motto is "No bullshit" and you can tell they really believe it. They have been very active in promoting open source projects, and give thousands of dollars away every year (in cash and services) to worthy projects they like to support. They have a very wide selection of domains and specialize in the newly-released vanity TLDs. And while they also offer VPSes, SSL certificates and shared hosting, they really shine in offering great prices for domains, a quality, dependable DNS service and expansive developer API. For me, Gandi has replaced all other providers of domain and DNS products because they are simply the best at what they do.

**Pros:**

* Unparalleled domain selection with volume pricing schemes
* Good company with great values
* Bills in euros, US dollars, Canadian dollars, etc etc

**Cons:**

* VPS pricing not as competitive
* New "v5" site upgrades aren't very stable yet


### Others

There are plenty of other options I've dabbled with in the past if none of the above options satisfies what you need. For dedicated servers, check out [Serverloft](http://serverloft.eu) or [Hetzner](https://www.hetzner.de/us/hosting/). Looking for VPSes? See [Bytemark](https://www.hetzner.de/us/hosting/) or [UpCloud](https://www.upcloud.com). For transactional email check out [Mailjet](https://www.mailjet.com), for DNS see [RAGE4](https://rage4.com), or for Heroku-like app hosting see [Scalingo](https://scalingo.com/pricing) or [Gandi](https://beta.gandi.net/en/simple-hosting).
