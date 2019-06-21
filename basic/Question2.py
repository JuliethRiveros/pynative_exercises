#

import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
v = a
for i in range(a+1,b+1):
	suma = i + v

	print(suma)
	v = i