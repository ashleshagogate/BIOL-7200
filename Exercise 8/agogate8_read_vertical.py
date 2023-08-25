#!/usr/bin/env python
import sys
line=""
c=0
n=int(sys.argv[1])
file=open(sys.argv[2],"r")
lines=file.readlines()
if n==0:
	print("The column number does not exist in the file")
	exit()
for i in range(0,len(lines)):
	line=lines[i]
	line=line.rstrip()
	words=line.split("\t")
	if n>len(words):
		print("The value is exceeding the file size")
		exit()
	else:
		print(words[n-1])


 
	
	
