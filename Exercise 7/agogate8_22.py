#!/usr/bin/env python
str=input("Enter the string ")
length=len(str)
open=0
close=0
for i in range (0,length):
	if str[i]=="{":
		open=open+1
	if str[i]=="}":
		close=close+1	
	if close>open:
		print("no")
		exit()
if open==close:
	print("yes")
else:
	print("no")
