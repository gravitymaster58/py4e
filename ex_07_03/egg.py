fn = input("Enter the file name: ")

fhand = open(fn)
for line in fhand:
    c = len(line)
    print(c)