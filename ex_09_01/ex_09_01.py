#complete
fn = ("words.txt")

fhandle = open(fn)

lst = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        if word not in lst:
            lst[word] = 1
        else:
            lst[word] += 1

print(lst)
