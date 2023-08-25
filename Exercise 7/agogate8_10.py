#!/usr/bin/env python
a = int(input("Enter the speed limit "))
b = int(input("Enter the speed of the vehicle "))
c = input("Is it their birthday? Enter yes or no ")
if c=="yes":
	diff = (b-5)-a
else:
	diff = b-a
if diff>0 and diff <= 15:
	print("The fine is small")
if diff>0 and diff > 15:
	print("The fine is large")
if diff<=0:
	print("There is no fine")




