<<<<<<< HEAD
#Complete
# Exercise 1: Write a simple program to simulate
# the operation of the grep command on Unix. Ask
# the user to enter a regular expression and count
# the number of lines that matched the regular expression:

ask = input("Enter a regular expression: ")
import re

fhandle = open("mbox.txt")
count = 0
for line in fhandle:
    line = line.rstrip()
    if re.search(ask, line):
        count += 1

print(count)
=======
fn = "regex_sum_42.txt"

fhandle = open(fn)

import re
numbers = list()

for line in fhandle:
    line = line.rstrip()
    numbers = re.findall(r'\d+',line)

    if len(numbers) >0:
        print(numbers)
>>>>>>> origin/master
