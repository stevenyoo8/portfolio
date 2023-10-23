#--------------------------------------------------#
# Title: Getting started with R
# Last date modified: 1/10/2023
#--------------------------------------------------#

# This file is called an R script (a file containing R code)
# Notice that this script is called "getstaRted.R" (see tab above)
# Think of R files (.R) as text files that contain R code

# Hashtags are used before text comments to explain what the code is for 
## You can put more than one if you want!

###############  Let's get staRted! ###############

#--------------------------------------------------#
## There are 4 panes in the R Studio window 
# This pane (top left) is the Editor pane, where you can edit the code

# Put your cursor anywhere on the line below and hit ctrl+enter 
# or click "Run" to submit code
print("welcome to R!")

# Notice how your output popped out on the bottom of your screen! 
# This is the Console!

#--------------------------#
## R as a calculator -------

6*6 # 6 times 6
6^2 # 6 squared
6*5*4*3*2*1 # 6 factorial
factorial(6)

#--------------------------#
## Functions ---------------

# Base R comes with many built-in functions
factorial(6) # better to use this function for calculating factorials
log10(10) # log base 10
exp(0) # exponential function (base e)
exp(1)
log(exp(1)) # unfortunately in R, "log" really means "ln" (log base e...)

# Try the function choose()
# If you need to know what arguments a function takes:
# type the function name, click inside of it, and hit tab
choose

# choose() takes two arguments n and k
choose(6,2)

# If you need to know what a function does, put a ? in front of the function name
?choose
# The documentation appears in the Output pane

#--------------------------#
## Objects -----------------

# The pane in the top right is the Environment. 
# This is where data, values, and created functions will go!
# There's nothing there yet because we haven't created any objects

# This notation "<-" is an assignment operator: 
school <- "UT Austin"
year <- 2023
happy <- TRUE

# Now do you see these objects in the Environment? 
# It saves what is on the right as an object whose name is on the left
school
# or more explicitly
print(school)

# You can also use "=" for assignment, but it is not recommended to do so
# This is because the double equal sign (==) is used for logical tests
# Try those:
2 == 2
2 == 3

# Object names... 
# start with a letter, 
# can’t contain spaces, 
# should not be predefined in R (e.g., do not label an object "log")

#--------------------------#
## Data types --------------

# Variables in R can be of different types.
# Use class() to check what type of objects we saved in the environment
class(school)
class(year)
class(happy)

#--------------------------#
## Vectors -----------------

# Create a vector: combine elements with c() which stands for concatenate
apple <- c('red','green',"yellow", "red") 
print(apple)
# Note that ' ' or " " can be used to define text

# Get the class of the vector
class(apple)

# Vector with numeric values
suite <- 100:150 # what does ":" do?
suite
class(suite)

# What if we have different data types in one vector?
x <- c(100, "France", 150)
class(x)
x

# R coerced the data into characters
# What if we want to coerce x as a numeric vector? What happens?
as.numeric(x)

#--------------------------#
## Data frames -------------

# A data frame is a very important data type in R = data structure for most tabular data
# can have different class variables
apples <- data.frame(
  variety = c('Gala', 'Granny Smith', 'Gold Delicious', 'Fuji'),
  color = c("red","green","yellow", "red"),
  sweetness = c(2, 4, 3, 1)
)
print(apples)

# Rows represent different observations, columns represent different variables
str(apples) # Use str() to get more information about an object

# You can access the different variables with $
apples$color

#--------------------------#
## Datasets ----------------

# Base R comes with many built-in datasets:
data()

# Let's take a look at this one:
women

# Try it! What type of data is the variable height in that dataset?
class(women$height)
summary(women)
str(women)

#----------------------------------------------------------#
## Other common objects: lists and matrices ----------------

# Create a list: combine many different types of elements inside a list
l <- list(school, year, happy, suite)
print(l)

# Create a matrix: 2-dimensional rectangular data set
# All data must be the same class
m <- matrix(c('Gala','red', 
              'Granny Smith', 'green', 
              'Gold Delicious', 'yellow',
              'Fuji', 'red'), 
            nrow = 4,  
            ncol = 2, 
            byrow = TRUE)
print(m)
# Note: matrices can only contain one type of data (try replacing 'red' by 1 for example)

#--------------------------#
## Indexing ----------------

# Recall our "suite" object
suite <- 100:150

# Index a specific value of a vector using [ ]
suite[1] # grab the first element
suite[10:20] # grab the 10th to 20th elements 
suite[c(10,20)] # grab only the 10th and 20th elements

# If we want to write the suite in descending order, we can reverse it and overwrite the old object.
suite <- rev(suite)
suite
# Now let's remove it momentarily with the rm() function
rm(suite)

# Get the suite object back by rerunning the line of code where you created suite
suite <- 100:150

# Let's add up all the values in the suite using the sum() function
sum(suite)

# How many values does our "suite" vector contain?
length(suite)

# We can add 1 to every data point (many operations are vectorized)
suite + 1

# We can multiply every original value by 2
suite*2

# What is the mean value of the suite? 
sum(suite)/length(suite)

# or using the built-in function
mean(suite)

# We can use indexing for data frames as well but we need to index 2 numbers: for rows and columns
# Recall our "apples" object
apples <- data.frame(
  variety = c('Gala', 'Granny Smith', 'Gold Delicious', 'Fuji'),
  color = c("red","green","yellow", "red"),
  sweetness = c(2, 4, 3, 1)
)
apples
# Index a specific row,column using [ ]
apples[1,2] # grab the first row, second column
apples[1, ] # grab the first row
apples[ ,2] # grab the second column

# Basic logical indexing: index on some conditions
apples[apples$color == "red", ] # only keep rows with color red
apples[apples$sweetness < 3, ] # only keep rows with top 2 sweetness

### [ROW, COL]

###############  Your turn! ###############

# Form a group of 6 students

# Part 1: Icebreaker questions
# Each student selects one question below and answers it
# a. How is your first week of classes going?
# b. If you were a wrestler, what would be your entrance theme song? 
# c. What is your spirit animal?

# Part 2: Collect and analyze data!
# a. Create a dataframe containing the following information
# - the names of your classmates in your group (including yourself)
# - their age
# - their height
# b. Find the mean age and height of students in your group. Report it here (copy/paste link in browser):
https://docs.google.com/spreadsheets/d/1hN_X4RvGw70EmIz4X883jzsIjv-UENWltDV4D_ctUr8/edit?usp=sharing
# c. Do you think all groups will get the same mean age? mean height? Why/Why not?

icebreaker <- data.frame(
  student_names = c("Steven", "Angelina", "CJ", "Amanda", "Glenda"),
  ages = c(21, 21, 21, 21, 22),
  heights = c(69, 63, 71, 64, 66)
)
icebreaker

mean(icebreaker$ages)
mean(icebreaker$heights)
