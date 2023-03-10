# Complete
# Exploring the HyperText Transport Protocol
#
# You are to retrieve the following document using the HTTP protocol
# in a way that you can examine the HTTP Response headers.
#
# http://data.pr4e.org/intro-short.txt
# There are three ways that you might retrieve this web page and
# look at the response headers:
#
# Preferred: Modify the socket1.py program to retrieve the above
# URL and print out the headers
# and data. Make sure to change the code to retrieve the above
# URL - the values are different for each URL.

import socket

url = input("Enter URL: ")

try:
    host = url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET ' + url +' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

except:
    print("The URL is improperly formatted or none existent")

mysock.close()