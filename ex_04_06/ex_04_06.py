def computepay(x, y):
    #print("In computepay", x, y)
    if x > 40:
        reg = x * y
        otp = 0.5 * y * (x - 40)
        pay = reg + otp
    else:
        pay = x*y

    return pay


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

p = computepay(h, r)

print("Pay", p)
