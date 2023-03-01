# Complete
# Exercise 2: This program counts the distribution of the hour of
# the day for each of the messages. You can pull the hour from the
# “From” line by finding the time string and then splitting that string
# into parts using the colon character. Once you have accumulated the
# counts for each hour, print out the counts, one per line, sorted by
# hour as shown below.


fn = "mbox-short.txt"

fhandle = open(fn)

times = dict()


for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()[5]
    time = words.split(":")[0]
    times[time] = times.get(time,0) + 1

lst = list()
for key, val in times.items():
    lst.append((key,val))

# print(lst)
lst.sort()
for item in lst:
    print(item[0], item[1])






