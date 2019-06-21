# Given a range of numbers. Iterate from o^th number to the end number and print the sum of the current number and previous number

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
v = a
for i in range(a+1,b+1):
	suma = i + v
	print(suma)
	v = i