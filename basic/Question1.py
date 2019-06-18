#Question1: Accept two int values from user and return their product.
#if the product is greater than 1000, then return their sum.

#Puedo usar la función input para esperar que el usuario ingrese un String.
a = int(input("Ingrese el número a: "))
b = int(input("Ingrese el número b: "))
producto = a*b
if (producto > 1000):
	suma = a+b
	print("la suma es", suma)
else:	
	print("el producto es", producto)