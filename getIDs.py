#/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from searchID import searchID

def getIDs(inputID):
	try:
		youtubeScript = urllib2.urlopen("https://www.youtube.com/watch?v=" + inputID)

		html = youtubeScript.read()

		str_token = 'adaptive_fmt'
		IDs = ""

		for line in html.split('\n'):
		# Get the code block where the javascript player locates.
			if str_token in line:
				javascript_player = line
				videoInfo = javascript_player.replace(";", ",");

				newVidInfo = ""
				for key in videoInfo.split(","):
				# Reorganize the code block to "key":"value", format
					if ':' in key:
						newVidInfo = newVidInfo + "\n" + key
					else:
						newVidInfo = newVidInfo + key + ", "

					for pair in newVidInfo.split('\n'):
					# Get to the code block where related videos locate.
						if "rvs" in pair:
							rvs_str = getReadable(pair.split(":")[1])
							IDs = searchID(rvs_str)
	
		return IDs
	except:
		return ""

