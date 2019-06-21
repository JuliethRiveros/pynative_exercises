#Given a range of numbers. Iterate from o^th number to the end number and print the sum of the current number and previous number

args <- commandArgs(trailingOnly = TRUE)

a <- as.numeric(args[2])
b <- as.numeric(args[3])
z <- a
for (i in (a+1):b){
	suma <- i+z	
	cat(suma,"\n")
	z <- i
}
