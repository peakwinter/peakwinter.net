---
title: Simple and fast static site blogging with KnockKnock
created_at: 2013-02-13 21:26:17 -0500
kind: article
tags: ["tech", "blogging", "nanoc", "static sites", "howto"]
---

I've recently replaced my old WordPress setup with a static site generator called nanoc. For those that don't know, a static site generator can use automated rules to create simple HTML pages based on the input you give it. These pages can be translated from an easy-to-write language like Markdown, making blogging with a static site generator very easy. It is also gaining popularing among "lightweight" bloggers like myself that don't require complicated search functions, PHP scripts or other slower and exploitable technologies. Its resulting simplicity is its greatest feature.

I will walk you through the features and functions of the custom framework of nanoc that I've created to easily host a functional blog. This framework is called KnockKnock.

<!-- more -->

KnockKnock is a framework that was cobbled together by me, mostly my own work and organization, but also borrowing bits from other corners of the nanoc blogosphere. I put it together after noticing that there was not really an easy way for someone starting out to get blogging with nanoc. This puts many different practices together to create a relatively simple yet cohesive and extensible framework.

![](/img/20130213001.png)

As of this post, KnockKnock features:

 * A front page with a list of recent posts and snippets of these posts
 * Posts with code syntax highlighting and "related articles" based on given post tags
 * Automatically-generated tag pages when new tags are added
 * An archives page, sorted by date and grouped by year (best for relatively-infrequent bloggers like many of us!)
 * Static "About Me" and "Projects" pages, and the ability to add more with relative ease
 * Social buttons for Github, Twitter, Email, and RSS
 * CSS theme inspired by the "[Left](https://github.com/holman/left)" theme for Jeykll by Zach Holman
 * Command to automatically create new posts with proper taxonomy, borrowed from [Jakob Lægdsmand](http://jakoblaegdsmand.com/blog/2013/01/easy-blogging-with-nanoc/) and modified

KnockKnock is still a work in progress, but I would definitely appreciate input from whoever would like to try it. You can find it on my GitHub page at [https://github.com/jacook/knockknock](https://github.com/jacook/knockknock). Feel free to take it apart, break it into tiny pieces, or even submit pull requests when you are able to make improvements.
