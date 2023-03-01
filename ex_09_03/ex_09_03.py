# Exercise 3: Write a program to read through a mail log,
# build a histogram using a dictionary to count how many
# messages have come from each email address, and print the dictionary.
# Completed

fn = "mbox-short.txt"

fhandle = open(fn)

emails = dict()

for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()[1]
    emails[words] = emails.get(words,0) + 1

print(emails)