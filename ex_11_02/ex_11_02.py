#InComplete
# Exercise 2: Write a program to look for lines of the form:
#
# New Revision: 39772
# Extract the number from each of the lines using a
# regular expression and the findall() method. Compute
# the average of the numbers and print out the average
# as an integer.
#
# Enter file:mbox.txt
# 38549
#
# Enter file:mbox-short.txt
# 39756


fhandle = open("mbox.txt")
import re

nums = list()

regex = "New Revision: (\d+)"
for line in fhandle:
    line = line.rstrip()
    if re.search('New Revision:' (\d+), line):
        print(line)