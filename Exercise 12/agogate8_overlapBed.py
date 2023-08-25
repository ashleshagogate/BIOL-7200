#!/usr/bin/env python3
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-i1")
parser.add_argument("-i2")
parser.add_argument("-m")
parser.add_argument("-j",action="store_true")
parser.add_argument("-o")
args=parser.parse_args()

input1=args.i1
input2=args.i2
min_overlap=args.m
join_option=args.j
output=args.o

min_overlap=int(min_overlap)

l1=[]
l2=[]
d1={}
d2={}
f=open(output, 'a')

file1=open(input1,"r")
rows1=file1.readlines()
for i in range(0,len(rows1)):
	row1=rows1[i].rstrip()
	row1=row1.split("\t")
	row1[1]=int(row1[1])
	row1[2]=int(row1[2])
	l1.append(row1)

file2=open(input2,"r")
rows2=file2.readlines()
for i in range(0,len(rows2)):
	row2=rows2[i].rstrip()
	row2=row2.split("\t")
	row2[1]=int(row2[1])
	row2[2]=int(row2[2])
	l2.append(row2)

i=0
k=0
while True:
	if i>=len(l1):
		break
	elif i==0:
		j=k
	elif l1[i][0]!=l1[i-1][0]:
		k=j
	j=k	
	while True:
		if j>=len(l2):
			i+=1
			j=k
			break
		if l1[i][0]!=l2[j][0]:
			if l1[i][0] != l1[i-1][0]:
				i+=1
				k=j
				break
			else:
				j+=1
				continue
		elif l1[i][0]==l2[j][0] and l1[i][1]!=l1[i][2]:
			if (l1[i][1]<l2[j][1] and l1[i][2]<l2[j][1]):
				i+=1
				j+=1
				break
			if (l1[i][1]>l2[j][1] and l1[i][1]>l2[j][2]):
				k=j
			if (l1[i][1]>l2[j][1] and l1[i][2]<l2[j][2]) or (l1[i][1]<l2[j][2] and l1[i][2]>l2[j][1]):
				overlap=(min(l1[i][2],l2[j][2])-max(l1[i][1],l2[j][1]))/(l1[i][2]-l1[i][1])
				percentage=100*overlap 
				if percentage>=min_overlap:
					if join_option==True:
						f.write(l1[i][0]+"\t"+str(l1[i][1])+"\t"+str(l1[i][2]))
						f.write("\t"+l2[j][0]+"\t"+str(l2[j][1])+"\t"+str(l2[j][2]))
						f.write("\n")
						i+=1
						j+=1
						break
					elif join_option==False:
						f.write(l1[i][0]+"\t"+str(l1[i][1])+"\t"+str(l1[i][2]))
						f.write("\n")
						i+=1
						j+=1
						break
				else:
					j+=1
			else:
				j+=1


