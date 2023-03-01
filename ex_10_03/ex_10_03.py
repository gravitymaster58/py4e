#Incomplete
# Exercise 3: Write a program that reads a file and prints
# the letters in decreasing order of frequency. Your program
# should convert all the input to lower case and only count the
# letters a-z. Your program should not count spaces, digits,
# punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and
# see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

fn = "mbox-short.txt"

fhandle = open(fn)

count = dict()
import string

for line in fhandle:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.digits))
    line  = line.lower()
    words = line.split()

    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] = +1

    lst = list()
    for key,var in count:




#     for word in words:
#         letters = words.split()
#
#     lst[letters] = lst.get(letters,0) + 1
#
#
# print(lst)