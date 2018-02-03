data <- read.table("stdin",header=F, skip=1)
dat <- t(data)
di2 <- (rank(dat[,1])-rank(dat[,2]))^2
out <- 1-(6*sum(di2))/(10*(10^2-1))
cat(round(out,3))