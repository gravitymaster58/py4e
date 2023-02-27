#completed
fname = "romeo.txt"
fh = open(fname)
lst = list()

for line in fh:
    line = line.rstrip()
    words = line.split()
    for word in words:
        if not word in lst:
            lst.append(word)

lst.sort()

print(lst[:])
