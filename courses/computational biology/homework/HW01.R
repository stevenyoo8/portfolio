url <- "https://utexas.box.com/shared/static/rrtbkan08hl7vgmffip87iv96splwq15.zip"
download.file(url,destfile = "chr4.depth.zip")
unzip(zipfile = "chr4.depth.zip")

samtools.depth <- read.table(file="chr4.depth.out", stringsAsFactors = F)
head(samtools.depth)
tail(samtools.depth)

View(samtools.depth)
class(samtools.depth)
summary(samtools.depth)
str(samtools.depth)
rownames(samtools.depth) #Returns the row names
colnames(samtools.depth) #Returns the columns names
dimnames(samtools.depth) #Returns a list of the row names and column names
nrow(samtools.depth) #Returns the number of rows
ncol(samtools.depth) #Returns the number of columns
dim(samtools.depth)  #Returns a integer vector of the dimension lengths
length(samtools.depth)
# This line extracts using the $ method and the column name
class(samtools.depth$V1)   
# This line extracts using the [ , ] method and the column index
class(samtools.depth[[2]])
# This line extract using the [ , ] method and the column name
class(samtools.depth[,"V3"]) 
col2 <- samtools.depth$V2
row13 <- samtools.depth[13,]
row13 
cell2_13 <- samtools.depth[13,2]
length(row13)
length(cell2_13)
length(row13)
col1 <- samtools.depth$V1
col2 <- samtools.depth$V2
col3 <- samtools.depth$V3
length(x = col1)
length(x = col1)
length(x = col2)
length(x = col3)
length(col1)
unlist(row13)
class(row13)
list(row13)
class(row13)
unlist(row13)
class(row13)
row13
row14
class(row14)
row13 <- samtools.depth[13,]
row13
class(col1)
unique(samtools.depth$V1) 
unique(samtools.depth$V3)
unique(samtools.depth)
chr4_group5_logic <- samtools.depth$V1 == "chr4_group5"
group5 <- samtools.depth[samtools.depth$V1 == "chr4_group5",]
group5
head(group5)
tail(x = group5)
chr4_group5_logic
chr4_group5_logic <- samtools.depth$V1 == "chr4_group5"
chr4_group5 <- samtools.depth[chr4_group5_logic, ]
chr4_group5
head(chr4_group5)
tail(chr4_group5)
unique(chr4_group5$V1)

samtools.depth[200001:250000,3]
x <- samtools.depth[200001:250000,3] 
mean(x)
sd(x)

dim(chr4_group5)
chr4_group1_logic <- samtools.depth$V1 == "chr4_group1"
chr4_group1 <- samtools.depth[chr4_group1_logic, ] 
chr4_group1
head(x = chr4_group1)
tail(chr4_group1)
dim(chr4_group1)
chr4_group1_logic
class(chr4_group1)
col3
col3 <- samtools.depth$V3
mean(col3)
sd(col3)
chr4_group5 <- samtools.depth[chr4_group5_logic, ]

summary(col3)
str(col3)
chr4_group5
col3
chr4_group1_logic
head(chr4_group5_logic)
chr4_group5

mean(col3)
mean(samtools.depth$V3)
group5col3 <- samtools.depth$V3[samtools.depth$V1 == "chr4_group5"]
group5col3
head(group5col3)
tail(group5col3)
summary(group5col3)
mean(group5col3)
sd(group5col3)


chr4_group1_logic <- samtools.depth$V1 == "chr4_group1"
chr4_group1 <- samtools.depth[chr4_group1_logic, ] 
head(chr4_group1)
tail(chr4_group1)

group1col3 <- samtools.depth$V3[samtools.depth$V1 == "chr4_group1"]
class(group1col3)
mean(group1col3)
sd(group1col3)


group5 <- samtools.depth
mean(group5col3)
sd(group5col3)
tail(group1col3)
tail(col3)
?hist

xlim=c(-5,max(chr4_group5$V3)) 
hist(x = group5col3, breaks = 150)
hist(x = col3, breaks = 150, col = "lightblue")
hist(x = col3,breaks = 150)
abline(v = mean(col3), col = "red")
abline(v = mean(group5col3), col = "red")

rnorm(n = 1000000, mean = 9.384, sd = 4.758)
rnorm(n = 1000000, mean = mean(group5col3), sd = sd(group5col3))
random.data <- rnorm(n = 1000000, mean = mean(group5col3), sd = sd(group5col3))
hist(x = random.data, breaks = 150, xlim = c(-5,max(chr4_group5$V3)))
hist(x = random.data, breaks = 150)
abline(v = mean(random.data), col = "red")
mean(random.data)
median(random.data)
mean(group5col3)
median(group5col3)

group2col3 <- samtools.depth$V3[samtools.depth$V1 == "chr4_group2"]
group5col3 <- samtools.depth$V3[samtools.depth$V1 == "chr4_group5"]
nrow(group5col3)
group2col3
tail(group2col3)
nrow(group5col3)
nrow(group1col3)
class(group2col3)
class(group5col3)

chr4_group2_logic <- samtools.depth$V1 == "chr4_group2"
chr4_group2 <- samtools.depth[chr4_group2_logic, ]

hist(x = group2col3, breaks = 75)
xlim=c(-5,max(chr4_group2$V3))
hist(x = group5col3, breaks = 150)
xlim=c(-5,max(chr4_group5$V3))
abline(v = mean(group2col3), col = "red")
qqnorm(y = group2col3)
qqline(y = group2col3, col = "red", lwd = 2)
qqline(y = group2col3, col = "red")

rnorm(n = 1000000, mean = mean(group2col3), sd = sd(group2col3))
random_data <- rnorm(n = 1000000, mean = mean(group2col3), sd = sd(group2col3))
hist(x = random_data, breaks = 125)
abline(v = mean(random_data), col = "red")

samtools.depth
row13 <- samtools.depth[13,]
unlist(row13)
row13
x <- unlist(row13)
class(x)
class(unlist(row13))

group5 <- samtools.depth$V3[samtools.depth$V1 == "chr4_group5"]
xlim=c(-5,max(chr4_group5$V3)) 
xlim=c(-5,max(group5)) 
hist(x = group5, breaks = 150)
abline(v = mean(group5), col = "red")

group2col3 <- samtools.depth$V3[samtools.depth$V1 == "chr4_group2"]
xlim=c(-5,max(group2col3))
hist(x = group2col3, breaks = 150)
abline(v = mean(group2col3), col = "red")
mean(group2col3)
median(group2col3)     
rnorm(n = 1000000, mean = mean(group2col3), sd = sd(group2col3))
random_data <- rnorm(n = 1000000, mean = mean(group2col3), sd = sd(group2col3))
hist(x = random_data, breaks = 120)
abline(v = mean(random_data), col = "red")
mean(random_data)
median(random_data)
summary(group2col3)
