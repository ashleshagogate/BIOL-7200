#!/usr/bin/env python
str=input("Enter the nucleotide sequence ")
str=str.upper()
print("The input sequence is ",str)
complement=""
l=[]
for i in str:
	if i == "A":
		l.append("T")
	if i == "T":
		l.append("A")
	if i == "G":
		l.append("C")
	if i == "C":
		l.append("G")
for x in l:
	complement+=x
print("The complimentary sequence is ",complement)
rev=str[::-1]
print("The reverse of the input sequence is ",rev)

if complement==rev:
	print("It is a palindrome")
else:
	print("it is not a palindrome")
