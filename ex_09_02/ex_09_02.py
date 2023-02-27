#incomplete

fn = ("Enter a file name:")

fhandle = open("mbox-short.txt")

counts = dict()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith("From"): continue
    words = line.split()


    if words[2] == 'Mon':
        counts['Mon'] += 1
    elif words[2] == 'Tue':
        counts['Tue'] += 1
    elif words[2] == 'Wed':
        counts['Wed'] += 1
    elif words[2] == 'Thu':
            counts['Thu'] += 1
        elif words[2] == 'Fri':
            counts['Fri'] += 1
        elif words[2] == 'Sat':
            counts['Sat'] += 1
        elif words[2] == 'Sun':
            counts['Sun'] += 1

print(counts)
