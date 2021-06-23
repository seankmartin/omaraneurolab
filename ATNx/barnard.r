install.packages("Exact", repos="https://cloud.r-project.org")

library("Exact")

method_to_use <- "Z-unpooled"

f_obs <- matrix(c(15, 0, 38, 47), nrow=2, ncol=2, byrow=TRUE)
result <- exact.test(f_obs, alternative="two.sided", method=method_to_use, model="Binomial", cond.row=FALSE)
result

f_obs <- matrix(c(16, 13, 37, 34), nrow=2, ncol=2, byrow=TRUE)
result <- exact.test(f_obs, alternative="two.sided", method=method_to_use, model="Binomial", cond.row=FALSE)
result