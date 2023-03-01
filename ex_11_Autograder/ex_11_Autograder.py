#Autograder


fn = "regex_sum_42.txt"

fhandle = open(fn)

import re
numbers = list()

for line in fhandle:
    line = line.rstrip()
    numbers = re.findall(r'\d+',line)

    if len(numbers) >0:
        print(numbers)