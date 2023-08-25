#!/usr/bin/env python3
import sys
pm=1
mism=-1
gap=-1
seq1=""
seq2=""

f1=sys.argv[1]
file1=open(f1,"r")
row=file1.readlines()[1:]
for i in range(0,len(row)):
	row[i]=row[i].rstrip()
for i in range(0,len(row)):
	seq1+=row[i]

f2=sys.argv[2]
file2=open(f2,"r")
row=file2.readlines()[1:]
for i in range(0,len(row)):
        row[i]=row[i].rstrip()
for i in range(0,len(row)):
        seq2+=row[i]


seq1list=[]
seq2list=[]

for i in seq1:
	seq1list.append(i)
for i in seq2:
	seq2list.append(i)


l1=len(seq1)+1
l2=len(seq2)+1

m=[]
for i in range(0,l1):
	mm=[]
	for j in range(0,l2):
		mm.append(0)
	m.append(mm)
t=[]
for i in range(0,l1):
	tt=[]
	for j in range(0,l2):
		tt.append(0)
	t.append(tt)

for i in range(1,l1):
	for j in range(1,l2):
		hv=(m[i][j-1])+gap
		vv=(m[i-1][j])+gap
		if seq1list[i-1]==seq2list[j-1]:
			dv=(m[i-1][j-1])+pm
		else:
			dv=(m[i-1][j-1])+mism
		maxval=max(hv,vv,dv)
		if maxval<0:
			m[i][j]=0
		else:
			m[i][j]=maxval
		if maxval==dv:
			t[i][j]="d"
		elif maxval==vv:
			t[i][j]="v"
		elif maxval==hv:
			t[i][j]="h"
start=0
index1=0
index2=0
for i in range(0,l1):
	for j in range(0,l2):
		if m[i][j]>start:
			start=m[i][j]
			index1=i
			index2=j
aseq1=""
aseq2=""

i=index1
j=index2

while (i>0 and j>0):
	pos=m[i][j]
	if pos==0:
		break
	if t[i][j]=="d":
		aseq1+=seq1[i-1]
		aseq2+=seq2[j-1]
		i=i-1
		j=j-1
	elif t[i][j]=="v":
		aseq1+=seq1[i-1]
		aseq2+="-"
		i=i-1
	elif t[i][j]=="h":
		aseq1+="-"
		aseq2+=seq2[j-1]
		j=j-1
align=""
score=0
revaseq1=aseq1[::-1]
revaseq2=aseq2[::-1]
for i in range(0,len(revaseq1)):
	if revaseq1[i]==revaseq2[i]:
		align+="|"
		score+=1
	elif revaseq1[i]!=revaseq2[i]:
		if revaseq1[i]=="-" or revaseq2[i]=="-":
			align+=" "
			score-=1
		else:
			align+="*"
			score-=1
	i=i+1


print(revaseq1)
print(align)
print(revaseq2)
print("Alignment score:",score)
	

	


