#!/usr/bin/env python3 
import subprocess
import argparse
import shlex
from multiprocessing import Pool
import sys

parser=argparse.ArgumentParser()
parser.add_argument("-o")
parser.add_argument("-t")
parser.add_argument('file',nargs='+')
args=parser.parse_args()

output=args.o
num_threads=args.t
if args.t==None:
	num_threads=1
ashley=open(output,'a')

l2=[]


l=args.file
l1=[" "]
for i in range(0,len(l)):
	l1.append(l[i])	
l2.append(l1)

def m(i):
	#l1=[l[i]]
	l1=[]
	if i>0:
		for k in range(0,i):
			l1.append("NA")
	for j in range(i,len(args.file)):
		if i==j:
			l1.append("100")
		else:
			command1="dnadiff -p result"+str(i)+str(j) + " " + str(args.file[i]) + " " + str(args.file[j])
			subprocess.check_output(shlex.split(command1))
			f="result"+str(i)+str(j)+".report"
			ps = subprocess.Popen(('head', '-19', f), stdout=subprocess.PIPE)
			output = subprocess.check_output(('tail', '-1'), stdin=ps.stdout)
			output=str(output).split()
			l1.append(output[1])
	return(l1)

			 
if __name__ == "__main__":
	pool=Pool(int(num_threads))
	outputlist=list(pool.map(m,list(range(0,len(l)))))
	heading=[" "]
	for i in range(0,len(l)):
		heading.append(l[i])
	for i in range(0,len(heading)):
		ashley.write(heading[i]+"\t")
	ashley.write("\n")

	for i in range(0,len(outputlist)):
		for j in range(0,len(outputlist)):
			if outputlist[i][j]=="NA":
				outputlist[i][j]=outputlist[j][i]
	#print(outputlist)
	k=0		
	for item in outputlist:
		ashley.write(l[k]+"\t")
		for j in range(0,len(item)):
			ashley.write(item[j]+"\t")
		k+=1
		ashley.write("\n")
	

