#!/usr/bin/env python

import sys

genes=[]
dict={}
my_list=[]
final_list=[]
output=[]
my_dict={}
output2=[]

x=open(sys.argv[3],"r")
lines=x.readlines()
for i in range(0,len(lines)):
	line=lines[i]
	gene=line.rstrip()
	genes.append(gene)

y=open(sys.argv[2],"r")
lines=y.readlines()
for i in range(0,len(lines)):
	line=lines[i]
	words=line.split("\t")
	dict[words[0]]=words[4]

z=open(sys.argv[1],"r")
lines=z.readlines()
for i in range(0,len(lines)):
        line=lines[i]
        words=line.split("\t")
        my_list.append([words[0],words[1],words[3],words[4]])

dict_subset = {key: value for key, value in dict.items() if value in genes}

for key,value in dict_subset.items():
	for k in range(0,len(my_list)):
		if key in my_list[k][0]:
			final_list.append([value,my_list[k]])

for i in range(0,len(final_list)):
	output.append([final_list[i][0],final_list[i][1][1],final_list[i][1][2],final_list[i][1][3]])  

for i in range(0,len(output)):
	if output[i][0] in my_dict.keys():
		continue
	else:
		my_dict[output[i][0]]=[output[i][1],output[i][2],output[i][3]]
print("Gene"+"\t"+"Chr"+"\t"+"Start"+"\t"+"Stop")
for i in sorted (my_dict):
	print(i+"\t"+my_dict[i][0]+"\t"+my_dict[i][1]+"\t"+my_dict[i][2])

