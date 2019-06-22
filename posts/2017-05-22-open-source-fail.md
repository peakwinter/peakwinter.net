---
layout: layouts/post.pug
slug: open-source-fail
title: "How to Fail at Open Source"
image: /assets/dist/images/20170521001.jpg
image_attribution: Given enough neglect, your projects will start to look like this soon enough. (<a href="https://www.flickr.com/photos/photosvincent/15791902902">Vincent Ferron</a>)
description: If the price you're paying is burnout, the product you're getting is worthless.
date: 2017-05-22
tags:
- open source
- projects
- development
- technology
- personal
---

Recently I discontinued my work on a big open source project I started a few years back called [arkOS](https://github.com/arkOScloud). This project brought me a lot of happiness and personal success over the years, some of which has [already been documented here](/blog/crowdfunding-campaign/). But several years after my initial successes, I found myself in command of a project that didn't at all resemble what it once was, or what I really wanted it to become. I was sapped of all energy and will to contribute to it, and felt any little bit I was able to do wasn't going to make a dent in the problem I was trying to solve, and would only further disappoint my users. This post is an exercise in taking stock of some of my failures with this project and the things I realized after I stopped working on it.

So, after nearly five years of open source contributions to this project, how did things get to this point?

### Promise The Moon

One of the biggest mistakes I made throughout the course of the project was in over-promising and under-delivering. It was a very common occurrence for me to receive messages on Twitter or on my project's forums that went a little something like this:

> Hey! I really like the idea of your project. But it would be awesome if it could do X. Then I'd use it full time. Is this kind of feature in progress?

So, in my eagerness to please, my response to messages like the above would often go: "Sure! I can start working on it right now! It'll be done in a month or so."

But who was I really kidding? It's far easy to assume that a feature will only take a day or so to complete, and sometimes that may actually be the case. But it's far more common that it takes two, three, four days or even more, given the unpredictable nature of developing such a large project. The end result is that I made a promise to a user that their desired feature would be implemented in a certain amount of time, I'm never actually able to get around to doing it in the expected timeframe, and then I ultimately (out of guilt) rush through production to get it done "soon enough." This is an atrocious flaw in professional software development, and even though the stakes are much lower in open source contributions, it is still a sure-fire way to frustrate your potential users and contributors.

**Solution: be pessimistic, then take off ten percent.**  When estimating anything, from an individual feature to the entire scope of your project, take the longest possible estimate you can make of when it would be done, then make that estimate ten percent longer. Don't worry about trying to keep up with the Joneses. Your reputation as a honest and dependable project manager is much more valuable than one that has good intentions but can only ever under-deliver.

### Do Everything At Once

The quickest way to set yourself up for failure is to bite off more than you can chew. Imagine a single developer trying to create their own open-source operating system, with an octopus-like modular API and software stack that deploys websites, creates encrypted disk partitions, configures network connections, binds to an LDAP server... but also someone that can find time to moderate a user forum, wiki, website, worldwide network of file servers, IRC channel, and much more.

This is what I tried to do alone. It's no wonder I had no time to contribute to a well-designed, iterative software development process that could yield a high-quality product. In retrospect this entire process would have been vastly easier if I limited my scope, and not tried to solve too many problems at once. Even if I had a small team of developers, my project could never hope to do so many things spectacularly well. Technical debt mounted at a fast pace because I didn't have the time to worry about essential things like unit tests or continuous integration &mdash; my time was taken up with just coding basic features.

**Solution: follow the [UNIX philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) whenever possible.** Break things down into achievable chunks, and don't be afraid of not doing everything you potentially could with a given project. Know your limits, as well as the limits of your team. Don't set the bar out of your own reach, and don't plan too far ahead.

### Don't Ask For Help

My specific problem was not necessarily that I wasn't asking for help (I actually did quite often), I just wasn't asking for help *from other people*. So I might as well not have asked for help at all.

My issues on Github were often in the style of, "Add authentication to X", "Refactor CSS", or one that was even just the cryptic title "Websockets". This is okay if I am going to be the one addressing these issues, because I know what all of those references mean. But nowhere in these issues was there information regarding how to reproduce the problem, which technical solutions might be used to implement the new feature, or where in the application one could look to find inspiration for the input I was seeking. At the end of the day, I wasn't asking for help the right way; I was asking for help from someone that already knew everything about the project (myself), and it was no wonder why I wasn't getting it!

So I never really took an honest look at why I wasn't getting the help I needed. My biggest need with the project was to find people qualified to assist with the development of core features. But nobody wants to spend several days learning the ins-and-outs of your software stack and trying to divine your intentions before they are even able to write a line of code.

**Solution: Be clear and specific with your needs, and facilitate the contribution process as much as possible.** Writing concise yet detailed explanations when documenting a new feature is essential. Otherwise it requires too much input from you before a new potential contributor can get started, and nobody wants to deal with that initial friction. While this process will take extra planning time from you, it is an essential investment that will bear fruit long-term.


### Be Afraid of Disappointment

When I first started my project, I was so excited by the prospect of helping people, and blinded by my own success, that I never really stopped to contemplate what I was doing. I simply had to trudge forward and continue my overarching mission: to deliver kickass software to people that really wanted it. My number one goal was always to make my users happy and proud of the work I was able to do with their support.

This isn't always the case with open source developers &mdash; some are only in it to solve a specific need they want to solve, and beyond that they don't much care if others get a lot of use out of it. And that's fine too. But that was never the way I operated. I took my user's needs very personally; I was invested in every one of them, and made it my personal mission to ensure that their experiences were always as positive as they could possibly be.

What did this mean concretely? On the positive side, I received constant compliments on my devotion to the ideas behind the project, as well as to the stellar tech support I was able to provide to my users through the forum and other means. On the negative side, my level of personal investment meant that I took every failure or misstep I made very seriously. Whenever I missed a self-imposed deadline, or I failed to properly fix a bug in a release, I took it as a source of shame and personal guilt.

The project itself then began to eat away at me. I would always have this nagging feeling, whenever I got home after a particularly stressful day at work and didn't feel like working on the project, that I was only going to miss another deadline and let down my users (my "fans", so to speak). Rather than being an avenue for worthwhile contributions to society, my project instead began to hang from my neck like an albatross, becoming something I dreaded having to work on because the weight of my own micro-failures outweighed all the positive reinforcement I was receiving.

**Solution: Don't ignore structural problems like the ones above, and don't take your failures too personally.** If the price you're paying is burnout, the product you're getting is worthless. If you are too invested in a specific commitment and can never be honest with yourself about the true causes of the problem, you're only going to make the emotional toll that much heavier, and contribute to a negative feedback loop. It's better to give up if you have to than to live with that stress in the back of your mind.


### Conclusion

I will admit that the title of this post is a bit over-the-top. I was able to accomplish a great deal with my project, and despite the fact that it never became anything close to what I wanted it to become, it taught me so much about software development and my own strengths and weaknesses. My aim with my next project is to better assess these problems as they happen, rather than after having created an inevitable burnout. I am going to try my best at being honest with myself about what I want to do, what I can do, and how best to involve the community at large rather than close myself in when I feel like I'm not achieving what I initially set out to do.

Making open source software is supposed to be a fun and valuable way to make contributions to society through one's technical skills as a developer. If you ever stop and realize that it isn't that way for you, you aren't doing it right!
