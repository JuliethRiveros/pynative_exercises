#Question 3: Accept string from the user and display only those characters which are present at an even index

import sys

a = sys.argv[1]
size = len(a)
for i in range(size):
	if i % 2 ==0:
		print(a[i])


# Using a while

i = 0
while i<size:
	print(a[i])
	i = i+2