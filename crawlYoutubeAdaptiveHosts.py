#!/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from getHost import getHost

parser = argparse.ArgumentParser('youtubeCrawler parser')
parser.add_argument('--id_file', action='store', dest='id_file', help='get a video id list to get corresponding urls.')
inputs = parser.parse_args()

outFile = open(inputs.id_file + "_adaptive_hosts.csv", 'w')
missIDFile = open("adaptive_host_miss_ids", 'w')
idFile = open(inputs.id_file, 'r')

for line in idFile:
	cur_id = line.replace("\n", "")
	url = getHost(cur_id)
	if not url:
		print cur_id + ": can not find adaptive streaming host!!"
		missIDFile.write(cur_id + "\n")
		missIDFile.flush()
		continue
	print cur_id + ", " + url
	outFile.write(cur_id + ", " + url + "\n")
	outFile.flush()

outFile.close()
missIDFile.close()

