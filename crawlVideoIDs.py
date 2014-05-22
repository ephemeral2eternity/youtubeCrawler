#/usr/bin/python

# Crawl youtube url

import string, argparse, urllib2, re, codecs
from getReadable import getReadable
from searchID import searchID
from getIDs import getIDs

parser = argparse.ArgumentParser('youtubeCrawler parser')
parser.add_argument('--seed', action='store', dest='seed_id', help='get a seed_id to start search youtube ids.')
parser.add_argument('--depth', action='store', dest='iter_num', help='get a depth of breadth first searching.')
inputs = parser.parse_args()
output = open(inputs.seed_id + '.ids','w')

i = 0
newList = [inputs.seed_id]
while (i < int(inputs.iter_num)):
	ID_List = sorted(set(newList))
	newList = []
	for inputID in ID_List:
		return_IDs = getIDs(inputID).split("\n")
		newList = newList + return_IDs
	print "depth = " + str(i)
	newList = sorted(set(newList))
	newIDs = ""
	refineList = []
	for id in newList:
		if len(id) == 11:
			newIDs = newIDs + id + "\n"
			refineList.append(id)
	newList = refineList
	output.write(newIDs)
	output.flush()
	i += 1

output.close()


