#!/usr/bin python
import sys

def parity(usrInput):
	count = 0
	byte = map(int,str(usrInput))
	if byte[-1] == 1:		
		for i in byte:
			if i == 1:			
				count += 1
		if (count-1) % 2 == 0:
			print ''.join(map(str, byte)) + " No errors"
		else:
			print("Error detected")
	elif byte[-1] == 0:
		for i in byte:
			if i == 1:
				count += 1
		if count % 2 != 0:
			print ''.join(map(str, byte)) + " No errors"
		else:
			print("Error detected")
	sys.exit()

parity(sys.argv[1])
