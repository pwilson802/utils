#! python
# lucky.py - opens several Google search results

import requests, sys, webbrowser, bs4

print('Googling....') # display test while downloading the google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# retrieve top search result links/
soup = bs4.BeautifulSoup(rest.text)

# Open a browser tab for each resultself
linkElems = soup.select('.r a')
numOpen = min(5, len(likElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
