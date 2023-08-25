#!/usr/bin/env python
x=0
y=1
c=1
fib = []
n=int(input("Enter the value of n "))
while c <= n:
       fib.append(x)
       z = x + y
       x = y
       y = z
       c += 1
print(fib)

