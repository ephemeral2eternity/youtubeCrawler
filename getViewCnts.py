#/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from searchID import searchID

def getViewCnts(inputID):
	try:
		youtubeScript = urllib2.urlopen("https://www.youtube.com/watch?v=" + inputID)

		html = youtubeScript.read()

		str_token = "watch-view-count"
		viewCnts = ""

		for line in html.split('\n'):
		# Get the code block where the javascript player locates.
			if str_token in line:
				view_cnt_line = removeWeirdCode(line)
				# print view_cnt_line	
				view_cnt_line = view_cnt_line.replace(" ", "&")
				view_cnt_line = view_cnt_line.replace(">", "&")
				view_cnt_line = view_cnt_line.replace("<", "&")
				view_cnt_line = view_cnt_line.replace(",", "")
				for word in view_cnt_line.split("&"):
					# print word
					if is_int(word):
						viewCnts = word
		return viewCnts
	except:
		return ""


def removeWeirdCode(s):
	uniString = unicode(s, "UTF-8")
	uniString = uniString.replace(u"\u00A0", "")
	s = repr(uniString)
	return s

def is_int(s):
	try:
		int(s)
		return True
	except:
		return False
