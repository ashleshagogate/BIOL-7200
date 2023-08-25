#!/usr/bin/env python
m = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]]
sum=0
count=0
l=[]
a=m[0]
for i in a:
	l.append(i)
b=m[1]
for i in b:
	l.append(i)
c=m[2]
for i in c:
        l.append(i)
print(l)
for i in range(0,15):
	for j in range(i+1,15):
		diff=l[i]-l[j]
		count=count+1
		sum=sum+diff
avg=sum/count
print("The average of pairwise differences is ",avg)
