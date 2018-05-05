from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import random

def getweb(url):
    try:
        html=urlopen(url)
    except HTTPError:
        print("HTTPError: page not found")
        return None
    if html is None:
        print("Error: service does not exist")
        return None
    return BeautifulSoup(html.read(),"html.parser")

def getlink(articleurl):
    page=getweb("http://en.wikipedia.org"+articleurl)
    return page .find("div", id="mw-content-text").find("p").find("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def looptest(init):
    print(init, end='→')
    link=getlink("/wiki/" + init)
    url=set()
    while True:
        print(link.attrs["href"][6::],end='→')
        url.add(link.attrs["href"])
        link = getlink(link.attrs["href"])
        if link.attrs["href"] in url:
            print(link.attrs["href"][6::],end='\n\n')
            break


looptest("Sun")
'''
looptest("Lead")
looptest("Canada")
looptest("Data")
looptest("Baroque")
looptest("Egg")
'''