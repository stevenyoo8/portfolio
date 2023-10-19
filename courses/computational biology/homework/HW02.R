qList <- list(first = 3:1,
              second = "hello",
              third = c(1:3, "hello"),
              fourth = data.frame("4.1"     = 1:4,
                                  Four.2    = 5:8,
                                  Four_Three = 9:12),
              fifth = matrix(12:1, nrow = 4, ncol = 3))
#Print to visualize
qList
View(qList)

length(qList)
print(qList)

qList$fourth[,c(FALSE, TRUE, FALSE)]

qList[[6]] <- 5
qList[[7]] <- 6
qList[[8]] <- 7
qList[[9]] <- 8

qList
list(qList, c("e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"))
list(qList, letters[5:15])
qList

qList$fourth$X4.1[1:3]
a <- qList$fourth$X4.1[1:3]
vectorA <- as.vector(x = a)
vectorA <- as.vector(x = qList$fourth$X4.1[1:3])
qList$fifth[4,]
b <- qList$fifth[4,]
vectorB <- as.vector(x = b)
vectorB <- as.vector(x = qList$fifth[4,])
qList$first
c <- qList$first
vectorC <- as.vector(x = c)
vectorC <- as.vector(x = qList$first)
vectorA + vectorB + vectorC

kmerSize  <- 6 #Numbers >>6 may cause memory issues
kmerDf
nucVector <- c("A", "C", "G", "T")
nucList   <- rep(list(nucVector), kmerSize)
kmerDf    <- expand.grid(nucList)
kmerDf$Pasted <- NA
kmerNrow  <- nrow(kmerDf)
for (i in 1:kmerNrow) {
  currRow          <- kmerDf[i, 1:kmerSize]
  currRow          <- unlist(currRow) # Needed to prevent paste0 converting the factors to their number values
  kmerDf$Pasted[i] <- paste0(currRow, collapse = "")
  if (i %% 1000 == 1) {
    iterPerc <- round(i / kmerNrow, 4) * 100
    print(paste0(i, "/", kmerNrow, " (", iterPerc, "%)"))
  }
}
## [1] "1/4096 (0.02%)"
## [1] "1001/4096 (24.44%)"
## [1] "2001/4096 (48.85%)"
## [1] "3001/4096 (73.27%)"
## [1] "4001/4096 (97.68%)"
head(kmerDf$Pasted)
## [1] "AAAAAA" "CAAAAA" "GAAAAA" "TAAAAA" "ACAAAA" "CCAAAA"
tail(kmerDf$Pasted)
## [1] "GGTTTT" "TGTTTT" "ATTTTT" "CTTTTT" "GTTTTT" "TTTTTT"

grep(pattern = "AT", x = kmerDf)
kmerDf[grep(pattern = "AT", x = kmerDf)]
grep("\\AT*",kmerDf)
kmerDf[grep("AT.*",kmerDf)]
grepl("AT",kmerDf, fixed = T)
kmerDf[grepl("AT",kmerDf)]
grep("T", kmerDf$Pasted)
kmerDf.EC <- kmerDf$Pasted[grep("^AT", kmerDf$Pasted)]
head(kmerDf.EC, 300)
View(kmerDf.EC)
kmerDf.EC
aa_error
