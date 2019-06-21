#Question1: Accept two int values from user and return their product.
#if the product is greater than 1000, then return their sum.

#Puedo usar la función input para esperar que el usuario ingrese un String.
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
producto = a*b
if (producto > 1000):
	suma = a+b
	print("la suma es", suma)
else:	
	print("el producto es", producto)