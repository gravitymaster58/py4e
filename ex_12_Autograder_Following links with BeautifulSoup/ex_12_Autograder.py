#Incomplete
#Following Links in Python

# In this assignment you will write a Python program that expands
# on http://www.py4e.com/code3/urllinks.py. The program will use
# urllib to read the HTML from the data files below, extract the
# href= values from the anchor tags, scan for a tag that is in a
# particular position relative to the first name in
# the list, follow that link and repeat the process a number of
# times and report the last name you find.
#
#
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

print(tags)
# tag_list= list()
# for tag in tags:
#     print("Retrieving: ", tag['href'])

# count = input("Enter count: ")
# position = input("Enter position: ")



# while count <4:
