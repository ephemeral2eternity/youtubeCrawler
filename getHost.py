#/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from searchID import searchID

def getHost(inputID):
	try:
		youtubeScript = urllib2.urlopen("https://www.youtube.com/watch?v=" + inputID)

		html = youtubeScript.read()

		str_token = 'adaptive_fmts'
		host = ""

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
						newVidInfo = newVidInfo + key + "&"

					for pair in newVidInfo.split('\n'):
						if str_token in pair:
							adaptive_fmts_str = getReadable(pair.split(":")[1])
							host = getUniqHost(adaptive_fmts_str)	
		return host
	except:
		return ""

def getUniqHost(adaptive_fmts):
	host_names = []
	hosts = ""
	for item in adaptive_fmts.split("&"):
		if "url" in item:
			try:
				cur_host = item.split("://")[1]
				cur_host_name = cur_host.split(".googlevideo.com")[0]
				host_names.append(cur_host_name)
			except:
				pass
	host_names = list(set(host_names))
	for host in host_names:
		hosts = hosts + host + ", "
	return hosts

