import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

# read url/link
url = 'http://py4e-data.dr-chuck.net/comments_1413573.xml'
uh = urllib.request.urlopen(url)
data = uh.read()

# render tree
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
# loop through nodes
count = 0
total = 0
for items in results:
    x = items.find('count').text
    new = int(x)
    print(new)
    count += 1
    total += new
print("Count: ", count)
print("Sum: ", total)
