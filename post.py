#!/usr/bin/python

import argparse
import datetime
import os
import re
import sys

CONTENT_PATH = '/home/jacob/Projects/Web/mysite/content/posts'

def add_status(status):
   # Parse the text, create a proper RST file in the good location
   number = 1
   oc = []

   now = datetime.datetime.now()
   for x in os.listdir(os.path.join(CONTENT_PATH, 'statuses')):
      if now.strftime('%Y%m%d%H%M') in x:
         number = number + 1
   path = os.path.join(CONTENT_PATH, 'statuses', 
      'status-%s%02d.rst' % (now.strftime('%Y%m%d%H%M'), number))

   links = re.findall('#([A-Za-z0-9]+)', status)
   status = re.sub('#([A-Za-z0-9]+)', '`\g<0>`_', status)

   title = 'Status %s%02d\n' % (now.strftime('%Y%m%d%H%M'), number)
   oc.append(title)
   oc.append('#' * len(title.rstrip('\n'))+'\n')
   oc.append(':date: %s\n' % (now.strftime('%Y-%m-%d %H:%M:%S')))
   oc.append(':tags: %s\n' % ', '.join(links))
   oc.append('\n')
   oc.append(status+'\n')
   oc.append('\n')
   [oc.append('.. _#'+link+': /tag/'+link+'\n') for link in links]
   oc.append('\n')
   
   f = open(path, 'w')
   f.writelines(oc)
   f.close()

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('-s')
   args = parser.parse_args()
   if args.s:
      add_status(args.s)
