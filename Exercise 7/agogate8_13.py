#!/usr/bin/env python
str=input("Enter the string ")
opt=input("Do you want to reverse the string? Type TRUE for yes and FALSE for no- ")
if opt == "TRUE":
	rev= str[::-1]
	print(rev)
elif opt == "FALSE":
	print(str)
else:
	print("Type TRUE for yes and FALSE for no")
