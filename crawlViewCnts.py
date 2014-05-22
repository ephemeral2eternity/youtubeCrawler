#!/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from getViewCnts import getViewCnts

parser = argparse.ArgumentParser('youtubeCrawler parser')
parser.add_argument('--id_file', action='store', dest='id_file', help='get a video id list to get corresponding urls.')
parser.add_argument('--version', action='store', dest='version', help='run version number of crawling')
inputs = parser.parse_args()

outFile = open(inputs.id_file + "_viewCnts_" + inputs.version + ".csv", 'w')
missIDFile = open("viewCnts_miss_" + inputs.version + ".ids", 'w')
idFile = open(inputs.id_file, 'r')

def is_int(s):
	try:
		int(s)
		return True
	except:
		return False

for line in idFile:
	cur_id = line.replace("\n", "")
	viewCnts = getViewCnts(cur_id)
	
	if not (is_int(viewCnts)):
		missIDFile.write(cur_id + "\n")
		missIDFile.flush()
		print cur_id + ": can not find view counts!!"
		continue
	
	print cur_id + ", " + viewCnts
	outFile.write(cur_id + ", " + viewCnts + "\n")
	outFile.flush()

outFile.close()
idFile.close()
missIDFile.close()
