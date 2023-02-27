#Not giving result correct result, but in autograder was correct..
fn = input("Enter file:")

fhandle = open(fn)
lst = dict()

for line in fhandle:

    if line.startswith("From:"):
        email = line.split()[1]
        lst[email] = lst.get(email, 0) + 1

max_emails = 0

max_address = None

for key in lst:
    if lst[key] > max_emails:
        max_emails = lst[key]
        max_address = key
print(max_address, max_emails)