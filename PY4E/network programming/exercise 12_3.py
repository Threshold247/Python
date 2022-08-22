import urllib.request
import urllib.parse
import urllib.error


url = 'http://data.pr4e.org/romeo.txt'
data = urllib.request.urlopen(url)

characters = 0
for line in data:     # loops through data
    # \n is considered a character
    # Amend to line.decode().rstrip() if needed
    words = line.decode().strip()  # decodes data
    # adds length of each paragraph to characters
    characters = characters + len(words)  # totals up characters
    if characters < 3000:  # only displays up to 3000 characters
        print(line.decode().strip())
print(characters)
