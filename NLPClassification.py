import urllib.request
from bs4 import BeautifulSoup

def GetAllDoxyDonkeyPosts(url, links):
    request=urllib.request.Request(url)
    response=urllib.request.urlopen(request)

    soup=BeautifulSoup(response)
    for a in soup.findAll('a'):
        try:
            url=a['href']
            title=a['title']
            if title =="Older Posts":
                print(title, url)
                links.append(url)
                GetAllDoxyDonkeyPosts(url, links)
        except:
            title=""
    return

blogUrl="http://doxydonkey.blogspot.in"
links=[]
GetAllDoxyDonkeyPosts(blogUrl, links)

