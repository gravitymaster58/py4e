fname = input("Enter file name: ")
fhand = open(fname)
count = 0
s = 0

for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        #print(line)
        s = s + float(line[20:])
        count = count + 1
        average = s/count


print("Average spam confidence: ",average)