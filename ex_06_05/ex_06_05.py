text = "X-DSPAM-Confidence:    0.8475"
numpos = text.find("0")
#print(numpos)
num = float(text[numpos:])
print(num)