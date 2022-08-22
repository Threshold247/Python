
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup


url = 'http://py4e-data.dr-chuck.net/known_by_Liana.html'
count = int(input("Enter count: "))
position = int(input("Enter position: "))-1

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
href = soup('a')
# print all links
#print(href)


for i in range(count):
    links = href[position].get('href', None)
    print(links)
    html = urllib.request.urlopen(links).read()
    soup = BeautifulSoup(html, 'html.parser')
    href = soup('a')
