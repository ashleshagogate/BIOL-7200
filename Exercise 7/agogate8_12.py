#!/usr/bin/env python
str=input("Enter a string ")
length=len(str)
if length%2==0:
	index=int(length/2)
	print(str[0 : index])
if length%2!=0:
	index=int((length/2)+1)
	print(str[0 : index])
