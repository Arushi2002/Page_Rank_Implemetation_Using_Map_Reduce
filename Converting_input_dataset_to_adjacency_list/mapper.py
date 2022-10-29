#!/usr/bin/env python3

import sys

#f_obj = open("sample_input.txt", "r")
#mo = open("map_out.txt", "w")
#w = open("w.txt", "w")

for f in sys.stdin:	
	if not f:
		break
	else:
		if(f[0] == "#"):
			continue
		source, dest = map(int,f.split("\t"))
		#w.write(str(source)+",1")
		print(f"{source}, {dest}")
		
