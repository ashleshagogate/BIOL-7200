#!/usr/bin/env python
l1=[]
l2=[]
sum1=0
sum2=0
n1 = int(input("Enter number of elements in list 1 : "))
print("Enter the elements (intergers only)")
for i in range(0, n1):
	x = int(input())
	sum1=sum1+x
	l1.append(x)
n2 = int(input("Enter number of elements in list 2 : "))
print("Enter the elements (intergers only)")
for j in range(0, n2):
	x = int(input())
	sum2=sum2+x
	l2.append(x)
if sum1==sum2:
	print("TRUE")
else:
	print("FALSE")
