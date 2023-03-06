# Complete
# Scraping Numbers from HTML using BeautifulSoup
# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers in the file.

#To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the span tags
tags = soup('span')
count = len(tags)
total = 0
numbers = list()

for tag in tags:
    number_list = re.findall(r'\d+\.\d+|\d+', tag.text)
    for number in number_list:
        numbers.append(int(number))

total = sum(numbers)

print("Count ", count)
print("Sum ", total)
