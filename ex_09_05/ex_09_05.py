# Completed
# Exercise 5: This program records the domain name (instead of the address)
# where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program,
# print out the contents of your dictionary.

fn = "mbox-short.txt"

fhandle = open(fn)

emails = dict()


for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()[1]
    school = words.split('@')[1]
    emails[school] = emails.get(school, 0) + 1

print(emails)

