# Completed
# Exercise 4: Add code to the above program to figure out who
# has the most messages in the file. After all the data has been
# read and the dictionary has been created, look through the
# dictionary using a maximum loop (see Chapter 5: Maximum and
# minimum loops) to find who has the most messages and print
# how many messages the person has.

fn = "mbox-short.txt"

fhandle = open(fn)

emails = dict()
max = 0
max_email = None

for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()[1]
    emails[words] = emails.get(words,0) + 1

    for word in emails:
        if emails[word] > max:
            max = emails[word]
            max_email = word
            

print(max_email, max)