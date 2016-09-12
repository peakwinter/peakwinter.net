---
layout: post
title: What I Learned Running a $53,000 Crowdfunding Campaign - By Myself
tags:
- personal
- professional
- technology
- journeys
- crowdfunding
- arkOS
- firestarter
---

A short time ago, I completed one of the largest challenges of my life to date. I set out to fund one year of development for my pet project, arkOS, bringing it from time-sucking yet worthy side project to a full-time employment opportunity, for at least the next year. I was fortunate enough to succeed at this venture, and I learned a great many things in the process.

The entire venture was exciting and terrifying, humbling and gratifying, in many different ways.

----

First off, if you are reading this post and you have no idea what my project is about, take a quick [read of this summary of arkOS by Jay Cassano](http://www.fastcolabs.com/3021919/open-company/finally-a-way-everyone-can-keep-their-data-from-the-nsa) posted in FastCompany a few weeks ago. It provides a great summary of the project, how it took off, and what it aims to become over the next few months.

In short, I decided to launch a crowdfunding campaign to help bring the project the time and attention it deserves. At the time I started the campaign, I was a part-time student at university, working nearly full time at a side-job as a systems administrator as well. All of my free time that I did have available was spent working on this side project. While I desperately wanted the project and the ideals behind it to succeed, I recognized that such a tedious school/work/life/project balanace wasn't going to end well. So I made the decision to launch a funding campaign, to let the people decide if the idea presented to them was worthy enough for their financial support.

Here are some of the most important things I learned throughout this process, and the challenges that I faced in bringing it to a successful completion.


### 1. I can't do everything.

There were many aspects of this campaign that humbled me, and for me that is something quite difficult to do. Not because I have such a lofty opinion of myself, quite the contrary - I have struggled with confidence issues for a very long time. But with that in mind, I am very much a "do-it-yourself" kind of person. It comes with the territory in the self-hosting field. I'm not often confronted with problems that, to paraphrase [Neckbeard Hacker](https://twitter.com/NeckbeardHacker), can't be solved "with a set of very small shell scripts". So the learning experience that this campaign gave me was a great time to evaluate my strengths and to learn a lot about how things work in this field. Media relations are a great example.

My idea was a good one, but the community around the project at that time was very small. It still is, to a certain degree. The project is a fairly hard-to-explain and frankly "geeky" concept as well. So I recognized early on that the goal wouldn't just be met via social networking prowess (you tell two friends and they tell two friends, etc). Because of this, I set an initial goal of getting at least *one* major media outlet to cover the project during the first week. I had a list of contacts, a compelling write-up and a high-quality media kit all put together. I had read many different "how to get noticed by *x* media outlet" guides before the campaign. I thought I had it all figured it out, and that I'd be beating them away with a stick after a few days' time. It's not like I was completely unprepared. But I might as well have been.

You see, getting media attention for your project is not a matter of will and effort, like I initially thought it would be. No, it is largely a matter of luck. When you send an email with your media kit to a journalist, your email is one of hundreds that they receive every day. Nobody could possibly filter through all of that every day and not be addicted to crack. The content matters in your message, you need to produce something that is attractive and compelling, and speaks to their core readership's desires. But at the end of the day, you could create the most kickass email in existence and never have it read. There's no heuristic email scanner that can pick out awesomeness. [1]

So during that first week of the campaign, I saw a great outpouring of support from people who were already loyal to the project, as well as the results from their eager posts on social media. But at the same time I saw that the "big" media push was indeed going to be critical. I stuck to my initial plan, ran through my contacts list (which included every major tech media outlet in the English-speaking countries), refined my message and did everything I possibly could to get noticed. I spammed their inboxes dozens of times in that first week. This resulted in very little success, compared to the vision I had going in. "But my project is awesome, and all of these people here agree with me," I reasoned. "I know their readers would be interested, how could I have not gotten a callback yet?" "Why is *x* media outlet posting about the 500,000th steampunk-themed Kickstarter and won't give my project a second look?" Be prepared for a lot of questions like this that don't really have good answers.

In the end, this push did result in the key for the campaign, and it was the combination of a refined message *and* a great deal of luck. Coincidentally it was an outlet that I had only sent one message to: VentureBeat. [2] They decided to do a feature on the project. My face was quickly plastered all over their front page, and it was the most popular story on the site for at least two or three days.

![VentureBeat home page](/assets/images/20131221001.png)

From there all of the other outlets that wrote about me did so without me reaching out first. And *then* I was beating them away with a stick. But the life lesson was that I'm not invincible. I can't control everything. There are problems that I simply cannot solve, no matter how small and well-commented my shell scripts are. And sometimes it is important to ask for help and add a bit of padding to one's expectations if you want to make it out with your nerves intact.


### 2. I'm certifiably insane.

I should point out here that *I had no reasonable clue that the project was going to succeed or not.* Which is pretty interesting given that I had committed to starting full-time work in January, meaning I had given my boss my departure notice and was basically one foot out the door. When you are living in a foreign country, far away from home and parental support, and you do something like this, it can be... pretty stressful.

On top of that, the funding site set up for the campaign was [entirely developed and operated myself](https://github.com/peakwinter/firestarter). I started work on it a mere couple weeks before the campaign was about to take off. It was pushed into production right as the buzzer sounded to begin the campaign on November 4th. I am not a newcomer to Python or Django, but running a site that was to get several thousand hits per day, managing a database of orders and other information, interacting with payment APIs for multiple providers? All of that was pretty new to me.

![Screenshot of the funding site](/assets/images/20131221002.png)

On top of *that*, I started the entire campaign in the month of November. A time when a lot of people are doing their Christmas shopping and are not as much concerned with ordering experimental goodies that they won't even see until next year. Also, a time where I start my year end finals in University, something that other students can understand is not the most leisurely experience in the world. Adding the full-time job of getting media coverage and maintaining the campaign website to an already busy plate was an interesting experience to say the least.

I had absolutely no idea how to do most of the things required of me in this campaign, up until it came time to do them. I had no PR specialists coaching me, no group of funding experts, no experienced VCs to bounce ideas off of. Nothing more than myself and a few *very* helpful friends to relay technical ideas. So most of the heavy lifting fell to me - the only one really behind the scenes. There were a lot of near-sleepless nights, always checking my phone, making sure that the site didn't catch fire and there wasn't a gang of rowdy people with pitchforks waiting outside for some reason. Days full of work, keeping the site responsive, interviews left and right, monitoring Twitter feeds, and a ton of worrying about every single possible minutia.

So the lesson here is that I can be much more audacious and risky than I initially thought. And it taught me that, hey, maybe I'm actually smarter and more capable than I think I am sometimes. [3] Any self-confidence issues that one has will take a back seat when you are thrust into taking such a large share of responsibility.


### 3. The Internet can be pretty cool.

Launching such a campaign doesn't just require a great deal of trust and commitment on the part of the person running it. It is also a lot to ask of each individual that is committing their hard-earned money for the cause. Especially when this is coming via crowdfunding, a medium of project financing that is gaining popularity, but still is treated with a very critical eye ([as it should be](http://pando.com/2013/06/30/thieves-and-scams-the-problem-with-crowdfunding/)). But by running a campaign, I was able to see how many people are willing to trust in an idea if it is well-articulated and confronts a certain need. People were willing to have confidence in me as I was willing to have confidence in them. It reinforced my belief in mutual aid and the underlying honesty in people.

It's easy to roll one's eyes when a young white male speaks to you about the "emancipatory power of the Internet". Such an idea must be treated with a great deal of criticism. But one area where the Internet can free us is in its capability to efficiently decentralize existing power structures. I was able to see how it is possible to build an alternative model for funding new technology - for producing quality and truly *free* software. No need for that boom-and-bust cycle of moving up and selling out, the heroin of Silicon Valley these days. Alternatives to capitalist investment and profiteering are as important now as ever, and if crowdfunding can be a piece of solving that puzzle, I'm happy to have been a guinea pig for it.

There are a lot of weird parts of the Internet that aren't very helpful for starting up new projects. People on public forum websites (like Reddit for example) can be downright mean when you ask for input on something you are working on. So you have to be careful when sharing your ideas, that you only give importance to the criticisms that are constructive. And to not take the entire experience personally, if it is negative one. The "trolling" tendency is something I've been acutely aware of for as long as I've been using the Internet. Which is why it was cool to see a different side of things - to encounter a community of people who are honestly energized by new ideas, who are willing to contribute to them if they believe, or at the very least to offer helpful and constructive criticism if they don't.

So in short, I learned a lot about the Internet and the people that use it. It has its bad sides, nobody should be deluded about that - but it also has a capacity to show the best qualities of individuals, and what they can accomplish when they come together. That last point is something that you don't see every day, so it is nice to be reminded of the positive aspects.


### Epilogue

If you hadn't followed the campaign over time, you would be interested to know that it achieved its funding goal of $45,000, and then some. The total amount raised was **$53,065**, a full 117% of the initial goal. Thanks so much to everyone who made this possible. You've made a huge difference for me, for free software, and for the future of easy and private self-hosted server systems.

[Check out the main project website](https://arkos.io) to learn more.


----

* [1] Someone should get on this, because it would make my life a lot easier.
* [2] THANK YOU VentureBeat!
* [3] Yes, that might contradict the first point a bit, but [it's not my job to be coherent].(http://www.brainyquote.com/quotes/quotes/w/waltwhitma132584.html)
