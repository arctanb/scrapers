#!/usr/bin/env python

import urllib
import urllib2
import os
import shutil
import sys

from BeautifulSoup import BeautifulSoup

# params

start_no = 300
end_no = 400
base_dir = 'files'


base_url = 'http://www.trancearoundtheworld.com/player/play.php?id='

def reporthook(count, blockSize, totalSize):
  percent = int(count*blockSize*100/totalSize)
  sys.stdout.write("%2d%%" % percent)
  sys.stdout.write("\b\b\b")
  sys.stdout.flush()

for i in range(start_no, end_no):
  url = '%s%d' % (base_url, i)
  bs = BeautifulSoup(urllib.urlopen(url).read())

  url = bs.findAll('audio')[0]['src']
  filename = '%s/tatw%d.mp3' % (base_dir, i)

  print '%s <- %s' % (filename, url)

  tmp_file, msg = urllib.urlretrieve(url, reporthook=reporthook)

  if os.path.exists(tmp_file) and os.path.getsize(tmp_file) > 50000000:
    shutil.copyfile(tmp_file, filename)
  print ''

  urllib.urlcleanup()

