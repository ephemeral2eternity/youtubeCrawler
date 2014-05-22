import string, re
from replaceASCII import replaceASCII

def getReadable( inputstr ):
	outputstr = inputstr.replace("\u0026", "&")
	outputstr = removeWeirdCode(outputstr)
	outputstr = replaceASCII(outputstr)
	outputstr = replaceASCII(outputstr)

	return outputstr

def removeWeirdCode(s):
	uniString = unicode(s, "UTF-8")
	uniString = uniString.replace(u"\u00A0", "")
	s = repr(uniString)
	return s
