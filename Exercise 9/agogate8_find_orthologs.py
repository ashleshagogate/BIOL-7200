#!/usr/bin/env python

import subprocess
import shlex
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-i1")
parser.add_argument("-i2")
parser.add_argument("-o")
parser.add_argument("-t")
args=parser.parse_args()

input1=args.i1
input2=args.i2
output=args.o
type=args.t

if type=="n":
	command1= "makeblastdb -in " + input1 + " -dbtype nucl -out db1"
	command2= "makeblastdb -in " + input2 + " -dbtype nucl -out db2"
	subprocess.check_output(shlex.split(command1))
	subprocess.check_output(shlex.split(command2))
	command3= "blastn -db db2  -query " + str(input1) + " -max_target_seqs 1 -outfmt 6 -out results1.txt" 
	subprocess.check_output(shlex.split(command3))
	command4= "blastn -db db1  -query " + str(input2) + " -max_target_seqs 1 -outfmt 6 -out results2.txt"
	subprocess.check_output(shlex.split(command4))
else:
	command5= "makeblastdb -in " + input1 + " -dbtype prot -out db1"
	command6= "makeblastdb -in " + input2 + " -dbtype prot -out db2"
	subprocess.check_output(shlex.split(command5))
	subprocess.check_output(shlex.split(command6))
	command7= "blastp -db db2 -query " + str(input1) + " -max_target_seqs 1 -outfmt 6 -out results1.txt"
	subprocess.check_output(shlex.split(command7))
	command8= "blastp -db db1 -query " + str(input2) + " -max_target_seqs 1 -outfmt 6 -out results2.txt"
	subprocess.check_output(shlex.split(command8))

f1 = open("results1.txt","r")
f2 = open("results2.txt","r")
result1 = {}
result2 = {}
for row in f1:
	row = row.split()
	result1[row[0],row[1]] = 1

for row in f2:
	row = row.split()
	result2[row[1],row[0]] = 1

final = {}
for key1 in result1:
	if key1 in result2:
		final[key1] = result1[key1]

with open(output, "w") as output_file:
	final = {k: v for k, v in sorted(final.items(), key=lambda item: int(item[0][1].split("_")[-1]))}
	for key in final:
		output_file.write(str(key[1]))
		output_file.write("\t")
		output_file.write(str(key[0]))
		output_file.write("\n")
