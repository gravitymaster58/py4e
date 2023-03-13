# Complete
# In this assignment you will write a Python program somewhat similar to
# http://www.py4e.com/code3/json2.py. The program will prompt for a URL,
# read the JSON data from that URL using urllib and then parse and extract
# the comment counts from the JSON data, compute the sum of the numbers in
# the file and enter the sum below:
import urllib.request, urllib.parse, urllib.error
import ssl

import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

while True:
    url = input('Enter location: ')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read()

    info = json.loads(data)
    print('Retrieved', len(data), 'characters')

    # print(info['comments'])
    print("Count: ", len(info['comments']))

    total = 0

    for item in info['comments']:
        total += int(item['count'])

    print("Sum: ", total)
    break