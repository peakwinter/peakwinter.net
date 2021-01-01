---
layout: layouts/post.pug
slug: time-machine-backupbundle-mount
title: "Recover Files from an Encrypted Time Machine Backup"
image: /assets/images/20210101001.png
description: Mounting an encrypted Time Machine backupbundle (macOS Catalina and later) as a drive to recover files, without using Migration Assistant.
date: 2021-01-01
tags:
  - howto
  - technology
  - apple
  - mac
  - macOS
  - backups
---

My Christmas gift to myself this year was a new M1 MacBook Pro, which runs lightning-fast and I'm very happy with it so far. It's my first newly-purchased laptop in forever, but I've had MacBooks for much of the past decade.

As you can imagine, this generates quite the Time Machine history. I use a [Synology DiskStation NAS](https://www.synology.com/en-ca/products/series/enthusiast) to act as a Time Machine drive as well as to hold all the movies, TV shows, photos and music I've acquired over the years that don't need to always go with me on my laptop's drive. The backup files here could use some cleaning as they currently weigh in at over 900GB in total. Yikes!

### Problem

When setting up the new MacBook, I wanted to try the Migration Assistant to restore from my Time Machine backup as I ended up trading in my last machine and couldn't transfer the files over from the old device. I left it running overnight and upon waking up the next morning the estimated completion time was still over 35 hours. Cue the "there HAS to be a better way!" memes.

Here's what I tried that **did not** work:

* **Double-click and mount the backup as a disk image:** This is not as straightforward as it sounds, as by default macOS tries to do disk integrity verification on every mount, and with the size of the drive we are talking it would just take forever and eventually fail with "no mountable filesystems".
* **Browse the contents of the backup as if it were a folder.** Many guides online reference ways to [access the `Backups.backupdb` folder hierarchy](https://www.devalias.net/devalias/2016/07/07/access-files-from-other-time-machine-backups/), which exists in the backup's sparsebundle file. sparsebundle is the format traditionally used for Time Machine backups; however back in macOS Catalina, Apple [changed the file format](https://eclecticlight.co/2019/11/14/time-machine-has-changed-again-in-catalina/) from a sparsebundle to a "**backupbundle**", which is essentially the same thing but in my case it doesn't have this `Backups.backupdb` allowing me to browse the filesystem as if it were real, perhaps due to the fact that my Time Machine backup is also encrypted.
* **Inherit the backup using `tmutil` and recover the files using the Time Machine app.** `tmutil` is [a command-line interface for some advanced Time Machine functions](https://eclecticlight.co/2020/01/22/time-machine-11-tmutil/), and it includes a subcommand called `tmutil inheritbackup` that is supposed to associate a backup from another system to your own, so that you can use the Time Machine app to browse the history and recover old files. In addition to its executions taking forever, this command ended up returning many cryptic errors including "no machine directories exist" and many others, and still wouldn't let me view my old files in the Time Machine app. Unfortunately this CLI is not well-documented and I didn't want to risk running other random commands with it in the case that it irrevocably corrupted my backup.
* **Mount the backup using a FUSE driver called [sparsebundlefs](https://github.com/torarnv/sparsebundlefs).** This appears to be made more for mounting sparsebundles in Linux, but I still tried it on macOS. It doesn't appear to support encrypted drives and gave me the same error about no mountable filesystems.

### Solution

In order to mount a Time Machine backupbundle that uses encryption, you must use **hdiutil** (a disk image mounting CLI included on all macOS machines) with some important flags:

```bash
hdiutil attach -noverify -nomount -readonly MyBackup.backupbundle
```

All of these flags are important: `-noverify` as otherwise it will do very long disk integrity checks before mounting; `-nomount` as you will mount it in a second step after the image is "attached" to ensure it's done in readonly mode; and `-readonly` as this seems to be required in order to successfully mount encrypted Time Machine backups -- all of my attempts without this flag took forever and eventually failed.

After executing this command, it will ask you for your backup encryption password. It will then print out a list of partition identifiers and filesystem types for the backup image it just attached. In my case, it looked like this:

```
/dev/disk4          	GUID_partition_scheme
/dev/disk4s1        	EFI
/dev/disk4s2        	Apple_HFS
```

Once the image is "attached" to your system, then run:

```bash
mkdir ~/mountfolder
mount -o ro -t hfs /dev/disk4s2 ~/mountfolder
```

Replace `/dev/disk4s2` with the partition identifier you got from `hdiutil attach`. The `-o ro` indicates to macOS that the disk image should only be mounted read-only, and `-t hfs` to tell it to mount your backups as an HFS drive (if the result of the above command is `Apple_APFS` then use `apfs` here instead).

Once you open the `mountfolder` directory in your home folder, you'll now see a `Backups.backupdb` folder containing a subfolder with your old computer's name, and under that some more subfolders for each date and time that Time Machine created a backup for. Pick the most recent folder and this should contain a symlinked reconstruction of your old computer's filesystem, with everything copyable to your new drive. In my case, I was able to get there with:

```bash
cd ~/mountfolder/Backups.backupdb/Epsilon/2020-11-23-004208/"Macintosh HD - Data"/
```

Enjoy!
