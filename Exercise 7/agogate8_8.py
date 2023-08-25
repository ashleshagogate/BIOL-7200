#!/usr/bin/env python
i=1
count=0
sum=0
average=0
max=0
min=0
while i==1:
	n=int(input("Enter the number "))
	if n == 0:
		print("The sum is ",sum)
		print("The average is ",average)
		print("The maximum is ",max)
		print("The minimum is ",min)
		exit()
	count+=1
	sum=sum+n
	average=sum/count
	if count == 1:
		max=n
		min=n
	else:
		if n>max:
			max=n
		if n<min:   
			min=n


