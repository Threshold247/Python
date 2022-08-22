import urllib.request
import urllib.parse
import urllib.error
import json

# read url/link
url = 'http://py4e-data.dr-chuck.net/comments_1413574.json'
uh = urllib.request.urlopen(url)
data = uh.read()
# convert to json dictionary
info = json.loads(data)
# extract comment object (list)
data = (info['comments'])

# loop through the list
count = 0
total = 0
for items in data:
    mycount = int(items['count'])
    print(mycount)
    count += 1
    total += mycount
print('Count: ', count)
print('Sum: ', total)
