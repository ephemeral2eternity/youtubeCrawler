#!/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from getViewCnts import getViewCnts
from getAllAttr import getAllAttr

parser = argparse.ArgumentParser('youtubeCrawler parser')
parser.add_argument('--id_file', action='store', dest='id_file', help='get a video id list to get corresponding urls.')
parser.add_argument('--locale', action='store', dest='location', help='run version number of crawling')
inputs = parser.parse_args()

outFile = open(inputs.id_file + "_allAttr_" + inputs.location + ".csv", 'w')
missIDFile = open("allAttr_miss_" + inputs.location + ".ids", 'w')
idFile = open(inputs.id_file, 'r')

def is_int(s):
	try:
		int(s)
		return True
	except:
		return False

for line in idFile:
	cur_id = line.replace("\n", "")
	attr = getAllAttr(cur_id)
	
	if not attr:
		missIDFile.write(cur_id + "\n")
		missIDFile.flush()
		print cur_id + ": can not find either view counts or adaptive streaming host!!"
		continue
	
	print cur_id + ", " + attr
	outFile.write(cur_id + ", " + attr + "\n")
	outFile.flush()

outFile.close()
idFile.close()
missIDFile.close()
