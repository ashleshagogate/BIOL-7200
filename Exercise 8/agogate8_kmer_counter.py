#!/usr/bin/env python
import sys
seq=""
m=sys.argv[1]
n=int(m)
fastq=sys.argv[2]
file=open(fastq,"r")
rows = file.readlines()[1:]
for i in range(0,len(rows)):
	rows[i]=rows[i].rstrip()
for i in range(0,len(rows)):
	seq+=rows[i]
list=[]
kmer=[]
count={}
for i in range (0,len(seq)):
	list.append(seq[i:(i+n)])
for item in list:
	if len(item)==n:
		kmer.append(item)
for i in kmer:
	if not i in count:
		count[i] = 1
	else:
		count[i] +=1
sortedcount=dict(sorted(count.items(), key=lambda x:x[0].lower()))
for i,j in sortedcount.items():
	print('{}\t{}'.format(i,j))




