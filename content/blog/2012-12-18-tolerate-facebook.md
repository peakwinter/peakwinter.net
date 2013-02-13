---
title: "Some (Almost) Guilt-Free Ways to Tolerate Facebook"
created_at: 2012-12-18 07:00:00 +0000
kind: article
tags:
   - internet
   - privacy
   - facebook
   - social networking
---

The holidays are an interesting time of year. Most of us spend our time with our families, catching up with stories or photos from the year past. Whether we love our families or... just 'like' them, Christmas often reminds us that we are stuck with them for life, for better or for worse. This fact is reinforced when we open up our Facebook profiles (for those of us that have them). Facebook has now become a social obligation for many family relationships. But for the privacy-aware user, Facebook is literally the worst-of-the-worst when it comes to tracking, commercialism and most other forms of corporate douchebaggery. The absolute best way is to just get rid of the thing once and for all. But if we can't get rid of our Facebook accounts due to social obligations, can we at least find a way to 'tolerate' it?

Here I will share how I use and configure my Facebook to be as minimally invasive as possible.

<!-- more -->

## 1. Use Ghostery to Block Facebook Trackers

Facebook operates a series of servers that are dedicated to tracking your movements across the web. Almost any site you visit nowadays has a little "Like" button. The "Like" buttons are not simply isolated images like other links on the web, but it is an embedded piece of code that gets executed on Facebook's servers. This provides Facebook with a detailed image of your browsing history as you move across the Web. Luckily for us, there is a fantastic extension for Firefox and Chrome called Ghostery. Ghostery lets you block not only Facebook trackers, but also a wide variety of tracking cookies and invasive analytic data used by countless other sites and platforms. This will eliminate a lot of Facebook's spying on your daily web use.

If you use Firefox, head to its [Firefox Add-ons page](https://addons.mozilla.org/en-US/firefox/addon/ghostery/), click "Add to Firefox," then follow the instructions. If you use Chrome, you can find it on its [Chrome Web Store page](https://www.google.ca/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;ved=0CCwQFjAA&amp;url=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fghostery%2Fmlomiejdfkolichcflejclcbmpeaniij%3Fhl%3Den&amp;ei=KKnQUMT5EMfaywHrp4CYBA&amp;usg=AFQjCNFXi-NAcIYeq985_Er7u2QSoFu-uw&amp;bvm=bv.1355534169,d.aWc). Once you have it installed, it will ask you a few questions based on what you will want to use it for. A good practice is to start with checking ALL boxes, which will block most online trackers by default. If you find a functionality you want to use later, you can always temporarily "pause" Ghostery, or you can only allow certain trackers via its search function.


## 2. Quit "Liking"!

A big way for Facebook to monetize you and your relationships is by using the pages you "like" in various ways. They can spread this information to any friends (or even friends-of-friends) that you have. Nothing is more embarrassing than your employer seeing that you once liked the "I'd rather have a 40 than a 4.0" group on Facebook. And really, what is the reason for "liking" pages anyway? If we merely want to use Facebook as a way to keep in touch with close friends and family, showing our allegiance to consumer brands or useless platitudes is redundant and a time-waster. Don't let Facebook and other corporations get rich off your data. Get rid of all your "liked" pages and deny Facebook an important (and invasive) revenue stream.


## 3. Manage your Applications

Again, if we are only going to use Facebook for personal contact, we have no use for the many applications that can pile up. These applications can have privileges to read our personal information and write on our Facebook walls. The best way to safeguard your privacy with regard to Facebook applications is to simply not use them. Clear out all of your unused Facebook applications, and revoke their access to your account. Use your Facebook page ONLY for communicating with your family and friends via messages or Wall posts. Keep any original content posted to Facebook (like photos via Instagram) to an absolute minimum.


## 4. Block Facebook Trackers at Your Firewall (For Extra Protection)

If you do not wish to use Ghostery for performance or other reasons, a more efficient way to block only Facebook trackers might be to do so at your firewall. The Facebook trackers have unique IP addresses that can track your outbound requests. These packets can be rejected at the firewall to improve performance and your online privacy.

If you use a Linux-based firewall, this is easy. UFW:

~~~
#!bash
sudo ufw reject out to 31.13.64.0/18
sudo ufw reject out to 66.220.144.0/20
sudo ufw reject out to 69.171.224.0/19
sudo ufw reject out to 69.63.176.0/20
~~~
{:.highlight}

or for Iptables:

~~~
#!bash
sudo iptables -A OUTPUT -d 31.13.64.0/18 -j REJECT
sudo iptables -A OUTPUT -d 66.220.144.0/20 -j REJECT
sudo iptables -A OUTPUT -d 69.171.224.0/19 -j REJECT
sudo iptables -A OUTPUT -d 69.63.176.0/20 -j REJECT
~~~
{:.highlight}

The downside to this method is that it is not as frequently updated as Ghostery. While Ghostery has a databse full of information that is relatively up-to-date, the IP addresses that Facebook use for tracking may be changed over time, requiring you to keep an eye on your settings and to consult the Internet regularly. If you need to update the trackers, you can see all Facebook's registered IP ranges by running:

~~~
#!bash
whois -h whois.radb.net '!gAS32934' | tr ' ' '\n'
~~~
{:.highlight}

Then try to visit a site that you know uses Facebook buttons or trackers. Check your firewall logs from this period for any of the IP addresses that come up with the above command, then add those IP ranges to your blocker. It takes a bit of work to do this, but depending on your configuration (like efficient blocking for an entire network), it may be worth it in the end.


## 5. Keep Privacy Settings Up-to-date

This should be an obvious one, but make sure your Privacy settings in Facebook are as restrictive as they can be. Facebook frequently changes the way they organize and display Privacy settings, so check back here every few months to make sure everything is just how you want it.

And last, but not least:

## 6. Encourage your Family and Friends to Head Elsewhere

Yes, yes, I know -- pulling a bull's teeth would be easier. But there are many social networks that are not as invasive and downright terrible as Facebook. Clearly and calmly explain your privacy concerns to your family, and explain why they should also be concerned. Offer to help them transition to new social networks that respect user privacy and ownership rights.

[Identi.ca](https://identi.ca) is a good alternative for sharing short messages, like on Twitter. [Diaspora](https://joindiaspora.com) is good for more Facebook-like features. The up-and-coming [Tent](http://tent.io) platform will also become more and more viable in the coming months. As I've repeated before: the best way to tolerate Facebook is to not use it at all.

---

Hopefully at this point we can use Facebook with at least a little more peace-of-mind. **These tips cannot resolve every problem Facebook has: it still can profit off the personal information and photos you deliver to it.** It may still be a painful experience, but as long as we are stuck with Facebook, we can ensure that it isn't stuck with us!
