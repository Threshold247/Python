import urllib.request
import urllib.parse
import urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_1413571.html'

data = urllib.request.urlopen(url)
headers = data.getheaders()
# print(headers)

# Neater layout
for header in headers:
    print(header[0], ':', header[1])
