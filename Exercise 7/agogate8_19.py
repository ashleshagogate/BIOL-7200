#!/usr/bin/env python
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
m = [[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15]]
for i in range (0,3):
	sum1=sum1+m[i][0]
	avg1=sum1/3
for i in range (0,3):
        sum2=sum2+m[i][1]
        avg2=sum2/3
for i in range (0,3):
        sum3=sum3+m[i][2]
        avg3=sum3/3
for i in range (0,3):
        sum4=sum4+m[i][3]
        avg4=sum4/3
for i in range (0,3):
        sum5=sum5+m[i][4]
        avg5=sum5/3
print("The mean of column 1 is ",avg1)
print("The mean of column 2 is ",avg2)
print("The mean of column 3 is ",avg3)
print("The mean of column 4 is ",avg4)
print("The mean of column 5 is ",avg5)
avg=(avg1+avg2+avg3+avg4+avg5)/5
print("The mean of means is ",avg) 
