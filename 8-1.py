#!/usr/bin python
count = 0

usrInput = raw_input("8 bit input: ")
byte = map(int,str(usrInput))

for i in byte:
	if i == 1:
		count += 1

if count % 2 == 0:
	byte += [1]
	print ''.join(map(str, byte))
else:
	print("Odd parity")
