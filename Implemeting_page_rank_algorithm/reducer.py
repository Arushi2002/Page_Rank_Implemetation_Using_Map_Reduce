#!/usr/bin/env python3

import sys
n=0
prev_q="-1"
q, contribution = "",""
rank=0.34

for i in sys.stdin:
	if not i:
		break
	
	i = i.split(",")
	q, contribution = i[0].strip(), i[1].strip()
	
	contribution=float(contribution)
	n+=1

	if(n == 1 and q != prev_q):
		rank+=0.57*contribution
		prev_q=q
	elif(n != 1 and q == prev_q):
		rank+=0.57*contribution
	elif(n != 1 and q != prev_q):
		rank=round(rank,2)
		print(prev_q+","+str(rank))
		prev_q = q
		rank=0.34+0.57*contribution

#Write the last node into w1.txt
rank=round(rank,2)
print(q+","+str(rank))



