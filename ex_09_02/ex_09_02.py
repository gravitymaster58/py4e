#Complete

fn = ("Enter a file name:")
fhandle = open("mbox-short.txt")

counts = dict()

for line in fhandle:
    if not line.startswith("From "): continue
    words = line.split()[2]
    counts[words] = counts.get(words, 0) + 1

print(counts)







