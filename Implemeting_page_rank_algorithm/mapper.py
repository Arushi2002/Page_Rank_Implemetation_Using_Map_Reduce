#!/usr/bin/env python3
import sys
import json

def similarity(p, q, cache):
	# Perform some initializations as required
	# Calculate the correct bounds using appropriate kernel_size 
	# (think about how big the size of p is to determine the ideal value).
	bound=len(p)
	kernel_size = 2
	bound =  bound - kernel_size + 1

	norm_q_2=0
	dot_p_q=0
	# print(bound)
	# print(p,q)
	# print(type(p))
	if cache is None:
		# Compute Dot product, Norms of p and q using loop unrolling. 
		# (Note you can compute everything in one loop unrolling segment).
		i=0
		norm_p_2=0
		i=0
		while i<bound:
			norm_p_2+=p[i]**2
			norm_q_2+=q[i]**2
			dot_p_q+=p[i]*q[i]

			norm_p_2+=p[i+1]**2
			norm_q_2+=q[i+1]**2
			dot_p_q+=p[i+1]*q[i+1]
		
			i+=kernel_size

		cache = norm_p_2
	else:
		# Compute Dot product, Norm of q using loop unrolling. 
		# (Note you can compute everything in one loop unrolling segment).
		i=0
		while i<bound:
			norm_q_2+=q[i]**2
			dot_p_q+=p[i]*q[i]

			norm_q_2+=q[i+1]**2
			dot_p_q+=p[i+1]*q[i+1]

			# norm_q_2+=q[i+2]**2
			# dot_p_q=p[i+2]*q[i+2]
		
			i+=kernel_size

	# Using the cache and Norm of q and the dot products, calculate similarity
	
	similarity=dot_p_q/(cache+norm_q_2-dot_p_q)
	#print(cache,norm_q_2,dot_p_q,similarity)
	return (similarity, cache) # pass the same cache again in subsequent calls.



w_file_path=sys.argv[1]
json_file_path=sys.argv[2]
#w_file_path='w.txt'
w=open(w_file_path,'r')

f=open(json_file_path)
data=json.load(f)
#aj=open('sample_output.txt','r')
for abc in sys.stdin:	
	if not abc:
	 	break
	else:
		#abc=aj.readline()
		cache=None
		p, li = abc.split("\t")
		li=li[1:len(li)-2]
		li=li.split(", ")
		line=w.readline()
		p_2,rank_p=line.split(",")
		p_2=p_2.strip()
		while(p!=p_2):
			line=w.readline()
			p_2,rank_p=line.split(",")
		if(p==p_2):
			rank_p=rank_p.strip()
			vector_p=data[p]
			print(f"{p}, 0.00")
			for q in li:
				
				vector_q=data[q]
				#print(p,q)
				similarity_p_q,cache=similarity(vector_p,vector_q,cache)
				#print(p,q,similarity_p_q)
				rank_p=float(rank_p)
				contribution_p_q=(rank_p*similarity_p_q)/len(li)
				print(f"{q}, {str(contribution_p_q)}")


f.close()
w.close()


