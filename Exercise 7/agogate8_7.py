#!/usr/bin/env python
a=10
b=30
print("Initial value of a is ",a)
print("Initial value of b is ",b)
temp=a
a=b
b=temp
print("Final value of a after using temp variable to swap is ",a)
print("Final value of b after using temp variable to swap is ",b)

a=10
b=30
a = a + b 
b = a - b
a = a - b
print("Final value of a without using temp variable to swap is ",a)
print("Final value of b without using temp variable to swap is ",b)

