#!/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from getHost import getHost
from getViewCnts import getViewCnts
from getAllAttr import getAllAttr

parser = argparse.ArgumentParser('youtubeCrawler parser')
parser.add_argument('--seed', action='store', dest='seed_id', help='get a video id list to get corresponding urls.')
inputs = parser.parse_args()

youtubeScript = urllib2.urlopen("https://www.youtube.com/watch?v=" + inputs.seed_id)
output = open(inputs.seed_id + '.rvs','w')

html = youtubeScript.read()

str_token = 'adaptive_fmt'

for line in html.split('\n'):
	if str_token in line:
		javascript_player = line


videoInfo = javascript_player.replace(";", ",");

newVidInfo = ""
for key in videoInfo.split(","):
	if ':' in key:
		newVidInfo = newVidInfo + "\n" + key
	else:
		newVidInfo = newVidInfo + key + "&"

# print newVidInfo

for pair in newVidInfo.split('\n'):
	if "rvs" in pair:
		rvs_str = getReadable(pair.split(":")[1])
		# print "rvs = " + rvs_str
	elif "url_encoded_fmt_stream_map" in pair:
		url_fmt_stream_map_str = getReadable(pair.split(":")[1])
		# print "url_fmt = " + url_fmt_stream_map_str
	elif "adaptive_fmts" in pair:
		adaptive_fmts_str = getReadable(pair.split(":")[1])


host = getHost(inputs.seed_id)
# print host

viewCnts = getViewCnts(inputs.seed_id)
# print viewCnts

allAttr = getAllAttr(inputs.seed_id)
print allAttr

output.write(rvs_str)
output.close()


