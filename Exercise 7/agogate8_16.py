#!/usr/bin/env python
l=[]
n = int(input("Enter number of elements in the list : "))
print("Enter the elements (intergers only)")
for i in range(0, n):
        x = int(input())
        l.append(x)
a = int(input("Enter the index position of the interger of choice "))
b = int(input("Enter the index position of another interger of choice "))
x=l[a]
y=l[b]
sum=x+y
prod=x*y
print("The sum is ",sum)
print("The product is ",prod)
