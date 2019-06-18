#Question1: Accept two int values from user and return their product.
#if the product is greater than 1000, then return their sum.

args <- commandArgs(trailingOnly = TRUE)

a <- as.integer(args[2])
b <- as.integer(args[3])

producto <- a*b

if (producto > 1000){
	suma <- a+b
	cat("La suma es", suma, "\n")
}else{
	cat("El producto es", producto, "\n")
}
