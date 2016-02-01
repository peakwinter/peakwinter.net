---
layout: post
title: Firefox OS and Geeksphone - First Impressions
tags:
- firefox os
- geeksphone
- peak
- mobile
- development
---

I've been lucky (and persistent) enough to get my hands on a Firefox OS development device, the Geeksphone Peak. This, along with its sister device the Keon, is the first Firefox OS device being sold to the general public. While it is not a "production" phone, I've found it to be a very snappy, fast and intuitive phone. Here are a few of my thoughts about both the device and its new developing operating system, their strengths and weaknesses.

### The Device

As the Geeksphone Peak is a developer device not intended for general use (yet), readers will have to take this section to be worth a grain of salt. But despite this, I still bought the device with the expectation that it will last a decent amount of time. The specifications it provides are sufficient enough for something like Firefox OS to run very well on, and I hope it will continue to serve me well into the future.

The device has many strong points. First off, it looks very good -- unremarkable yet classic white/black colour, smooth lines, nothing out of the ordinary but accomplished very well. The cute "Firefox OS Developer Preview" insignia is on the back in orange, a very nice touch.

The microphone, earphone and loudspeaker work excellently. Clear and concise. I was surprised at how loud the loudspeaker could get to while listening to music. Might be good for using in the park with friends. The battery life is not fantastic, but decent. I am able to use the phone casually throughout the day with calls and texts with no risk of it dying on me. As more features of Firefox OS become available, I might use it for more things like browsing Tent or checking my email. I don't expect this use to dramatically effect battery life but it might become more difficult to manage.

Its cameras work as well as can be expected for a device of this price. The front-facing camera is a definite improvement over the camera on my old phone (a Samsung Galaxy S, original version). The photo below was taken with this camera. It also has a front-facing camera, leading me to hope for a future open source voice chat app to be ported to Firefox OS in the future. This front-facing camera is somewhat low quality, matching what a video chat might look like over an Internet connection.

![Geeksphone Peak](/assets/images/20130617011.jpg)

There are a couple of points that make the phone less desirable. Reception isn't the best: I can only get 3/5 bars in my apartment, which is in the middle of the second biggest city in Canada, and where my old phone gets 5/5 bars consistently. I hope I don't get stranded if I decide to take trips with this phone! The screen is susceptible to a weird sort of refresh problem, but only in certain Firefox OS widgets. In the main Settings menu, a faint "ghost image" of past screens can be visible in the menu bar, but after I switch applications once or twice this goes away. The battery cover is pretty strange. You have to pull very hard in order to get it off, it comes off all in one piece. I thought I was going to break it the first time I did it, but it does have a bit of flex and can deal with the punishment. It doesn't seem like it was very well engineered.

Overall, though, these things are just minor annoyances that can be lived with as long as the rest of the phone continues to work as well. And as long as I continue to love its operating system, which I will get into now.

### Firefox OS

![Firefox OS home screen](/assets/images/20130617001.jpg)

Firefox OS is a breath of fresh air in a rather congested mobile operating system environment. One of my biggest complaints with Android to this point has been its performance. I do have an older phone, I will admit that, but even loading simple applications or doing something as shocking as loading a webpage on my phone (*gasp*) can be a painful experience. When I check through the resources that each application is using, even for supposed "lightweight" ones, it's staggering.

With Firefox OS, everything is a "web app". I'm consistently stunned with how fast everything is, even on a device with meager specifications compared to the latest-and-greatest Android or iOS devices. The browser (also called Firefox) is lightning-fast, not just in starting up but also in loading webpages.

So there are two kinds of applications: ones that you launch from a pane (pictured below) that looks somewhat like a glorified Bookmarks toolbar, then you have the "regular" apps you can get from the Marketplace. One of my issues with this distinction is that it is not very clear to the end user. Yes, you have the Marketplace app, which loads a specific kind of web app that gets installed to the home page, then you have this pane which loads websites themselves, but they can *also* be pinned to the regular app screens with an app icon and acting just like an app. The end result is, you can have two Twitter icons on your home screen, both supported by Twitter and using the same-ish kind of interface. In actuality, one is an official Firefox OS application and the other is just the website version. If this sounds confusing, it's because it is. If you load other websites that don't look as good from this pane, like the Gmail mobile site, a user might think it's an "app" when it is not, it's just a shoddy looking mobile site. The distinction between this bookmarks pane and the real Marketplace app could be made clearer.

![Bookmarks pane](/assets/images/20130617002.jpg)

Something which exacerbates this issue on my phone: the Peak's larger aspect ratio isn't yet handled well by Marketplace apps. Below, you can see the Marketplace version of the Twitter app on the left, and the Twitter mobile website on the right. Both are viewed from the same phone, but only the mobile site is properly sized. This is an issue that I face with all marketplace apps, including the Marketplace itself. This makes most Marketplace apps nearly unusable for me. I can't imagine that Mozilla wouldn't address something like this, though, so I'm sure it is just a passing annoyance while the OS is in development.

![Twitter app](/assets/images/20130617005.jpg)
![Twitter mobile website](/assets/images/20130617006.jpg)

Calls are handled very well, with a familiar yet clean interface. It works quickly and dependably, just what you need when actually using your phone for phone-things. Contacts lack CardDAV sync capability, and the editing screen for individual contacts is a bit clunky, but I'm sure these will be smoothed out in time. Presently you can only add Contacts from Facebook; I haven't tried this as I no longer have a Facebook account.

![Incoming call](/assets/images/20130617003.jpg)
![On the call](/assets/images/20130617004.jpg)

The Calendar app is pretty slick, I can tell that a good deal of effort has gone into it thus far. It already has CalDAV sync support which is awesome for linking it with my ownCloud instance I have at home. Creating and viewing events works very well so far, even managing multiple synced calendars with ease. The menu bar is a little annoying, though: it's not very responsive to touch, which might be a problem with my phone's screen but I'm not sure. Also the menu button on the left is too small, This menu bar is the same as is in all of the Gaia base apps (Calendar/Email/Messages/etc), so these little problems persist across apps.

![Calendar app](/assets/images/20130617007.jpg)

Firefox OS also has a cool Maps application called "HERE Maps". This is actually an app produced by Nokia but it is entirely web-based and works very well. Featuring most of the features that Google Maps provides, like directions, transit maps and traffic layers. It also has a voice commands feature; I haven't tried it out yet but that is still very impressive. You can see that it is also subject to the screen sizing issue as I explained before, but aside from that it looks great.

![HERE Maps](/assets/images/20130617008.jpg)

I was also quite surprised by how well the Music app works already. It pulls album art in from your music folders and displays them in the standard grid-file. It already has album views, shuffle and repeat capability, and plays seamlessly in the background. There are a few things I'm waiting for: namely an equalizer, smooth transitioning between songs, and Last.FM integration. Some better music library views (like PowerAMP for Android, my preferred music app, has) would also be nice. I am sure that other music apps will eventually be created and I am eager to see what they can come up with.

![Music app](/assets/images/20130617009.jpg)


The (Non-Final) Verdict
-----------------------

I'm really excited about these efforts to more closely merge mobile use with the fantastic developments in web technologies we've seen over the past 5-10 years. Not only can it deliver faster performance for a lower price, something that will greatly aid developing countries and people getting online for the first time, but it will also hopefully drive down our dependence on constantly "upgrading" to the newest and fastest devices. I look forward to Firefox OS helping to extend the lifespan of our devices, making society less wasteful but still inspired by what improvements that the Internet can bring to our lives. As with any project in development, there are a few bugs here and there, but with an open source mobile operating system we actually have hope that these bugs will be addressed and worthy improvements can be made.

No need to put up with Google, Microsoft and Apple's walled gardens any longer -- the future is here, and it's *fast* :)
