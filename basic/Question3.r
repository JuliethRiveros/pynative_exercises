#Question 3: Accept string from the user and display only those characters which are present at an even index

args <- commandArgs(trailingOnly = TRUE)

a <- args[2]
size <- nchar(a)
for (i in 1:size){
	if (i %% 2 == 0){
		cat(substr(a, i, i),"\n")
	}
}