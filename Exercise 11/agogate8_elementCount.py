#!/usr/bin/env python3
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("-i", help="This takes in a bed file as the input and returns the number of times each genomic coordinate occurs")
args=parser.parse_args()
input=args.i
list=[]
chromosome=[]
file=open(input,"r")
row=file.readlines()
for i in range(0,len(row)):
	row[i]=row[i].rstrip()
	row[i]=row[i].split("\t")
	list.append(row[i])

for i in range(0,len(list)):
	if list[i][0] not in chromosome:
		chromosome.append(list[i][0])

for p in chromosome:
	d={}
	l=[]
	for i in range(0,len(list)):
		if (list[i][0]==p):
			start=int(list[i][1])
			end=int(list[i][2])
			chr=list[i][0]
			for j in range(start,end):
				c=1
				if j in d.keys():  
					c=int(d[j])
					c+=1
					d[j]=c
				else:
					d[j]=c

	sorteddict=dict(sorted(d.items(), key=lambda x:x[0]))
	for i,j in sorteddict.items():
		l.append([i,j,chr])

	k=0
	while True:
		if k>=len(l):
			break
		i=k
		begin=l[k][0]
		count=l[k][1]
		y=0
		j=k
		while True:
			i=k
			if j==len(l):
				stop = int(l[j-1][0])+1
				print(chr+"\t"+str(begin)+"\t"+str(stop)+"\t"+str(count))
				break
			if (int(l[i][1])==int(l[j][1])) and (int(l[i][0])==(int(l[j][0])-y)):
				y+=1
				j+=1
				continue
			else:
				stop=int(l[j-1][0])+1
				print(chr+"\t"+str(begin)+"\t"+str(stop)+"\t"+str(count))
				k=j
				break
		if j==len(l):
			break		

								


		
		
		
		


		

