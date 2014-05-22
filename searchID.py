import argparse, string, re


def searchID( inputStr ):
	ids = ""
	for vid in inputStr.split(","):
		for vidInfo in vid.split("&"):
			if "id=" in vidInfo:
				curID = vidInfo.split("=")[1]
				if len(curID) == 11:
					ids = ids + vidInfo.split("=")[1] + "\n"
	return ids


# parser = argparse.ArgumentParser('inputfile for rvs ids')
# parser.add_argument('--input', action='store', dest='inputfile', help='get an inputfile for rvs ids.')

# inputargs = parser.parse_args()
# inputStr = open(inputargs.inputfile, 'r').read()

# ids = searchID(inputStr)
# print ids

