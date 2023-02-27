fname = "mbox-short.txt"


fhand = open(fname)

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):



        print(line)