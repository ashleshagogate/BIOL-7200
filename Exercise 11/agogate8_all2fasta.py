#!/usr/bin/env python3
import re
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-i",help="The input files can be of fastq,embl,genbank,vcf,sam or mega format")
parser.add_argument("-f",help="This depicts the folding while printing the sequence. The default value is 70")
args=parser.parse_args()

input=args.i
input_split=input.split(".")
filename=input_split[0]

fold=args.f
if fold==None:
	fold=70
fold=int(fold)

file=open(input,"r")
row=file.readlines()

str=row[0]
str1=row[1]
if str.startswith("ID"):
	kind="embl"
elif str.startswith("LOCUS"):
	kind="gb"
elif str.startswith("##"):
	kind="vcf"
elif str.startswith("@") and str1.startswith("@"):
	kind="sam"
elif str.startswith("@"):
	kind="fastq"
elif str.startswith("#"):
	kind="mega"

if kind=="embl":
	l=str.split()
	des=">"
	final=""
	list=[]
	for i in range(1,len(l)):
		des=des+l[i]
	for i in range(0,len(row)):
		if row[i].startswith("SQ"):
			sequence=row[i+1:len(row)]
	
	for i in range(0,len(sequence)):
		seq=sequence[i]
		seq=seq.rstrip().lstrip(" ")
		list=seq.split()
		for j in range(0,(len(list)-1)):
			f=list[j]	
			final=final+f
	final=final.upper()
	characters=["A","C","G","T","N","a","c","g","t","n"]
	xtn="fna"
	for i in range(0,len(final)):
		if final[i] in characters:
			continue
		else:
			xtn="faa"
			break
	output=filename+"."+kind+"."+xtn
	f=open(output, 'a')
	f.write(des)
	f.write("\n")
	k=0
	while True:
		if k>=len(final):
			break
		f.write(final[k:k+fold])
		f.write("\n")
		k=k+fold
							
if kind=="gb":
	str1=row[3]
	str2=row[1]
	l1=str1.split()
	l2=str2.split()
	des=">"
	final=""
	list=[]
	for i in range(1,len(l1)):
		des=des+l1[i]
	for i in range(1,len(l2)):
		des=des+" "+l2[i]	
	for i in range(0,len(row)):
		if row[i].startswith("ORIGIN"):
			sequence=row[i+1:len(row)]
	for i in range(0,len(sequence)):
		seq=sequence[i]
		seq=seq.rstrip().lstrip(" ")
		list=seq.split()
		for j in range(1,len(list)):
			f=list[j]	
			final=final+f
	final=final.upper()
	characters=["A","C","G","T","N","a","c","g","t","n"]
	xtn="fna"
	for i in range(0,len(final)):
		if final[i] in characters:
			continue
		else:
			xtn="faa"
			break
	output=filename+"."+kind+"."+xtn
	f=open(output, 'a')
	f.write(des)
	f.write("\n")
	k=0
	while True:
		if k>=len(final):
			break
		f.write(final[k:k+fold])
		f.write("\n")
		k=k+fold
if kind=="mega":
	for i in range(1,len(row)):
		if row[i].startswith("#"):
			str1=row[i]
			des=">"
			final=""
			list=[]
			sequence=[]
			for j in range(1,len(str1)):
				des+=str1[j]
			des=des.strip()
		
			for n in range(i+1,len(row)):
				if row[n].startswith("#"):
					break		
				else:
					sequence.append(row[n])

			for j in range(0,len(sequence)):
				seq=sequence[j]
				seq=seq.rstrip()
				list=seq.split()
				for k in range(0,len(list)):
					f=list[k]	
					final=final+f
			final=final.upper()
			characters=["A","C","G","T","N","a","c","g","t","n"]
			xtn="fna"
			for m in range(0,len(final)):
				if final[m] in characters:
					continue
				else:
					xtn="faa"
					break
			output=filename+"."+kind+"."+xtn
			f=open(output, 'a')
			f.write(des)
			f.write("\n")
			k=0
			while True:
				if k>=len(final):
					break
				f.write(final[k:k+fold])
				f.write("\n")
				k=k+fold

if kind=="fastq":
	final=""
	list=[]
	seq=""
	for i in range(0,len(row)):
		if row[i].startswith("@"):
			des=">"
			str1=row[i].rstrip()
			for j in range(1,len(str1)):
				des=des+str1[j]
		if re.findall(pattern="^[ATGCNatgcn]+$", string=row[i]):
			seq=seq+row[i]
			seq=seq.strip()
		elif re.findall(pattern="^[ARNDCEQGHILKMFPSTWYVarndceqghilkmfpstwyv]+$", string=row[i]):
			seq=seq+row[i]
			seq=seq.strip()
		elif row[i].startswith("+"):
			seq=seq.strip()
			seq=seq.upper()
			characters=["A","C","G","T","N","a","c","g","t","n"]
			xtn="fna"
			for i in range(0,len(seq)):
				if seq[i] in characters:
					continue
				else:
					xtn="faa"
					break
			output=filename+"."+kind+"."+xtn
			f=open(output, 'a')
			f.write(des)
			f.write("\n")
			k=0
			while True:
				if k>=len(seq):
					break
				f.write(seq[k:k+fold])
				f.write("\n")
				k=k+fold
			seq=""
			continue
if kind=="sam":
	list=[]
	for i in range(0,len(row)):
        	r=row[i]
        	if r.startswith("@"):
                	continue
        	else:
                	r=r.split("\t")
                	list.append(r)
	for i in range(0,len(list)):
		des=">"
		id=list[i][0]
		seq=list[i][9]
		des=des+id
		characters=["A","C","G","T","N","a","c","g","t","n"]
		xtn="fna"
		for j in range(0,len(seq)):
			if seq[j] in characters:
				continue
			else:
				xtn="faa"
				break
		output=filename+"."+kind+"."+xtn
		f=open(output,'a')
		f.write(des)
		f.write("\n")
		k=0
		while True:
			if k>=len(seq):
				break
			f.write(seq[k:k+fold])
			f.write("\n")
			k=k+fold
if kind=="vcf":	
	list=[]
	ref=[]
	alt1=[]
	alt=[]
	seq=""
	xtn="fna"
	output=filename+"."+kind+"."+xtn
	f=open(output,'a')
	for i in range(0,len(row)):
		r=row[i]
		if r.startswith("##"):
			continue
		else:
			r=r.split("\t")
			list.append(r)
	
	chrom=list[1][0]
	for i in range(0,len(list)):
		ref.append(list[i][3])
		alt.append(list[i][4])

	for i in range(1,len(ref)):
		seq=seq+ref[i]
	f.write(">"+chrom)
	f.write("\n")
	k=0
	while True:
		if k>=len(seq):
			break
		f.write(seq[k:k+fold])
		f.write("\n")
		k=k+fold

	for i in range(0,len(alt)):
		x=alt[i].split(",")
		alt1.append(x)
	for i in range(9,len(r)):
		y=[]
		sample=[]
		sample1=[]
		seq1=""
		for j in range(0,len(list)):
			sample.append(list[j][i])
		for k in range(0,len(sample)):
			y=sample[k].split(":")
			sample1.append(y[0])
		sample_name=sample1[0].strip()
		f.write(">"+sample_name)
		f.write("\n")
		for m in range(1,len(sample1)):
			z=int(sample1[m])
			if z==0:
				seq1=seq1+ref[m]
			else:
				seq1=seq1+alt1[m][z-1]
		k=0
		while True:
			if k>=len(seq):
				break
			f.write(seq1[k:k+fold])
			f.write("\n")
			k=k+fold
		
		
					
			
			
