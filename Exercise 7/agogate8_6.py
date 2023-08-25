#!/usr/bin/env python
c=input("Enter the character of choice ")
for i in range (1,6):
  for j in range (1,i+1):
    print (c , end="")
  print("\r")  
for i in range (1,5):
  for j in range (4,i-1,-1):
    print (c , end="")
  print("\r")
