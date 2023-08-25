#!/usr/bin/env python
m = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]]
print("The original matrix is ")
print(m)
a=m[0]
a.reverse()
b=m[1]
b.reverse()
c=m[2]
c.reverse()
m = [a,b,c]
print("The reversed matrix is ")
print(m)
