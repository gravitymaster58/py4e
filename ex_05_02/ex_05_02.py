smallest = None
largest = None

while True:

    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        ival = int(sval)
        smallest = 1000
        largest = -1000
        if ival < smallest:

            smallest = ival

        elif ival >largest:
            largest = ival


    except:
        print("Invalid input")
        continue

print("Maximum is ", largest)
print("Minimum is ", smallest)