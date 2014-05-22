import string, re

def replaceASCII( inputstr ):
	asc_code = re.findall("%..", inputstr)
	asc_code = sorted(set(asc_code))

	outputstr = inputstr
	for asc in asc_code:
        	asc_val_str = asc.split('%')[1]
		try:
        		asc_val = chr(int(asc_val_str, 16))
        		outputstr = re.sub(asc, asc_val, outputstr)
    		except:
        		pass

	return outputstr
