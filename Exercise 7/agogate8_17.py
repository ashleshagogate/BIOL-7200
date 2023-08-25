#!/usr/bin/env python
l=[]
n = int(input("Enter number of odd elements in the list : "))
print("Enter the elements (intergers only)")
for i in range(0, n):
        x = int(input())
        l.append(x)
l.sort()
length=n-1
pos=int(length/2)
median=l[pos]
print("The median is ",median)
