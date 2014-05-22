#/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from searchID import searchID
from getHost import getUniqHost

def getAllAttr(inputID):
	try:
		youtubeScript = urllib2.urlopen("https://www.youtube.com/watch?v=" + inputID)

		html = youtubeScript.read()

		viewCnt_token = "watch-view-count"
		player_token = "adaptive_fmts"
		viewCnts = ""
		host = ""

		for line in html.split('\n'):
			if viewCnt_token in line:
				view_cnt_line = removeWeirdCode(line)
				view_cnt_line = view_cnt_line.replace(" ", "&")
				view_cnt_line = view_cnt_line.replace(">", "&")
				view_cnt_line = view_cnt_line.replace("<", "&")
				view_cnt_line = view_cnt_line.replace(",", "")
				for word in view_cnt_line.split("&"):
					if is_int(word):
						viewCnts = word
						# print viewCnts

			elif player_token in line:
                                javascript_player = line
                                videoInfo = javascript_player.replace(";", ",");
                                newVidInfo = ""
                                for key in videoInfo.split(","):
                                # Reorganize the code block to "key":"value", format
                                        if ':' in key:
                                                newVidInfo = newVidInfo + "\n" + key
                                        else:
                                                newVidInfo = newVidInfo + key + "&"

                                for pair in newVidInfo.split('\n'):
                                        if player_token in pair:
                                                adaptive_fmts_str = getReadable(pair.split(":")[1])
                                                host = getUniqHost(adaptive_fmts_str)
						# print host

		if host and viewCnts:
			attr = viewCnts + ", " + host
		else:
			attr = ""

		return attr
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
