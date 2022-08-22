import urllib.request
import urllib.parse
import urllib.error

from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1413571.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
total = 0

tags = soup('span')
for tag in tags:
    # .contents refers to value inside link e.g <p>this value</p>
    numbers = int(tag.contents[0])
    print('Numbers: ', numbers)
    count = count + 1
    total = total + numbers

print('Count: ', count)
print('Total: ', total)
