#!/usr/bin/env python3

import sys

n = 0
prev_source = "-1"
cur_source, cur_dest = "",""
source, dest = "",""

file_path=sys.argv[1]
w = open(file_path, "w")


for i in sys.stdin:
	if not i:
		break
	#i = i[1:len(i)-1].split(",")
	i = i.split(",")
	source, dest = i[0].strip(), i[1].strip()

	n+=1

	if(n == 1 and source != prev_source):
		print(source+"\t"+"["+dest, end = "")
		prev_source=source
		w.write(str(source)+",1\n")
	elif(n != 1 and source == prev_source):
		cur_source, cur_dest = i[0].strip(), i[1].strip()
		print(", "+cur_dest, end = "")
	elif(n != 1 and source != prev_source):
		print("]")
		prev_source = source
		print(source+"\t"+"["+dest, end = "")
		w.write(str(source)+",1\n")

w.close()
print("]")
