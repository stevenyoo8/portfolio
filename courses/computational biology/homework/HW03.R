url <- "https://utexas.box.com/shared/static/rrtbkan08hl7vgmffip87iv96splwq15.zip"
fileName <- "chr4.depth.out"
if (!file.exists(fileName)) {
  zipName <- paste0(fileName,".zip")
  download.file(url,destfile = zipName)
  unzip(zipName,files = fileName)
}
samtools.depth    <- read.table(fileName,stringsAsFactors = F)
samtools.depth$V2 <- as.numeric(samtools.depth$V2)
samtools.depth$V3 <- as.numeric(samtools.depth$V3)
View(samtools.depth)

#Q4
class(samtools.depth)
samtools.depth[samdepth0,]
samdepth0 <- samtools.depth$V3[samtools.depth$V3=="0"]
samdepth0
samtools.depth[samtools.depth$V3=="0",]

#Q5
samtools.depth.gte11RD <- samtools.depth[samtools.depth$V3 > 10,]
nrow(removed)
head(samtools.depth.gte11RD)
tail(samtools.depth.gte11RD)

#Q6
chr4grp2Lte5k.logic <- samtools.depth$V1=="chr4_group2" & samtools.depth$V2 < 5001
head(samtools.depth[chr4grp2Lte5k.logic, ])
tail(samtools.depth[chr4grp2Lte5k.logic, ])
class(chr4grp2Lte5k.logic)
length(chr4grp2Lte5k.logic)  
sum(chr4grp2Lte5k.logic)

#Q8
samtools.depth[samtools.depth$V1 == "chr4_group3",]
q8 <- samtools.depth$V1 == "chr4_group3" & samtools.depth$V3 == "0"
samtools.depth[q8,]
head(samtools.depth[q8,])
tail(samtools.depth[q8,])
head(samtools.depth[samtools.depth$V1=="chr4_group3",])
tail(samtools.depth[samtools.depth$V1=="chr4_group3",])
endposition <- 150000-147006
startposition <- 113592-100001
startposition - endposition


install.packages("maps")
library("maps")
class(us.cities)
cities <- us.cities
View(us.cities)

#Q9
grepl(pattern = "^San .*", us.cities$name)
san_city <- grepl(pattern = "^San .*", us.cities$name)
us.cities[san_city, 1]

#Q10
no_space_city <- gsub(pattern = " ", replacement = "", cities$name)
no_state_city <- gsub('.{2}$','', no_space_city)
no_state_city <- gsub('.{3}$','', cities$name)
tail(sort(table(no_state_city)))

#Q11
unique(no_state_city)
low_case <- tolower(no_state_city)
unique(low_case)

#EC1
min(us.cities$long)
us.cities[us.cities$long == "-157.8", ]

#EC2
max(us.cities$long)
us.cities[us.cities$long == "-69.77", ]

#EC3
us.cities$pop > 200000
ec3 <- us.cities[us.cities$pop > 200000, ]
x <- us.cities[us.cities$pop > 200000, ]
x <- ec3[[1]]
(unique(x))

#EC4
grep('in$', no_state_city, value = T)
               
#EC5
grepl("a.* .*n", no_state_city)
grep("o.* .*o",bentley)

#Q3
library("ggplot2")
p1<-ggplot(data = samtools.depth, mapping = aes(x = V2,y = V3))+ 
  # Draws a red vertical line
  geom_vline(xintercept = 25730,color="red")+
  # Plots a 2d-histogram of RD vs position colored by frequency.
  geom_bin_2d(binwidth = c(500,2))+
  # Seperates the plots based on the contig
  facet_wrap(facets = vars(V1),ncol = 1)+
  # Changes the fill color scaling to my favorite color-blind friendly palette
  scale_fill_viridis_c()+
  # Changes various formatting to my favorite settings
  theme_bw()+
  # Modifies the axis labels
  labs(x="Position (bp)",y="Read-depth")

# Saves the plot to file
ggsave(filename = "samToolPosVsRd.png",plot = p1,
       width = 15,height = 15,units = "in",dpi = 300)
p1

