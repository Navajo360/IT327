#!/usr/bin python
import sys

count = 0

def evenOdd(usrInput, parity):
	if parity == 'e':
		byte = map(int,str(usrInput))
		count = 0
		for i in byte:
			if i == 1:
				count += 1
		if count % 2 == 0:
			byte += [1]
			print ''.join(map(str, byte))
		else:
			print("Odd parity")
	
	elif parity == 'o':
		byte = map(int,str(usrInput))
		count = 0
		for i in byte:
			if i == 1:
				count += 1
		if count % 2 != 0:
			byte += [0]
			print ''.join(map(str,byte))
		else:
			print("Even parity")
	sys.exit()

evenOdd(sys.argv[1], sys.argv[2])
