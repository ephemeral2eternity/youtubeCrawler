#!/usr/bin/python

# Hello world python program
# print "Hello World!";

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from replaceASCII import replaceASCII

parser = argparse.ArgumentParser('youtubeCrawler parser')
parser.add_argument('--seed', action='store', dest='seed_id', help='get a seed_id to start search youtube ids.')
inputs = parser.parse_args()

youtubeScript = urllib2.urlopen("https://www.youtube.com/watch?v=" + inputs.seed_id)
output = open(inputs.seed_id + '.adaptive_fmt','w')

html = youtubeScript.read()

str_token = "adaptive_fmt"

for line in html.split('\n'):
	if str_token in line:
		javascript_player = line

for key in javascript_player.split(','):
	if str_token in key:
		adaptive_fmt = key

print adaptive_fmt

adaptive_fmt = adaptive_fmt.replace('\u0026', '&')
adaptive_fmt_items = adaptive_fmt.split(':')
adaptive_fmt_value = adaptive_fmt_items[1]

print adaptive_fmt_value

adaptive_fmt_value = replaceASCII(adaptive_fmt_value)
adaptive_fmt_value = replaceASCII(adaptive_fmt_value)

print adaptive_fmt_value

output.write(adaptive_fmt_value)
output.close()


