hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter Rate:")
r = float(rate)

regpay = h * r

if h > 40:
    otpay = regpay + 0.5 * r * (h - 40)
    print(otpay)

else:
    print(regpay)


