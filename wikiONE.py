'''
By Xiangxin Kong May 5th
This program will get the first link in the main text of a Wiki page,
and then repeating the process for subsequent pages.
It's inspired by article: Wikipedia:Getting_to_Philosophy
(https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy)
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re

def getweb(url):
#this function accept a link as string.
#If the url is valid,it return the page as a beautifulsoup object.
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
#this function accept a wiki page link
#if the link is correct,it will return the first link in the main text.
    page=getweb("http://en.wikipedia.org"+articleurl)
    if page is None:return None
    return page .find("div", id="mw-content-text").find("p").find("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def looptest(init):
#this function accept the title(string-) of the initial page.
#if the page respect to the title excist, it will print the title
#and then try for the first link of current page, until the page repeat.
    link = getlink("/wiki/" + init)
    if link is None: return True
    print(init, end='→')
    url=set()
    while True:
        print(link.attrs["href"][6::],end='→')
        url.add(link.attrs["href"])#save the url of the pages it has visited
        link = getlink(link.attrs["href"])
        if link.attrs["href"] in url:
            print(link.attrs["href"][6::])
            print('(It takes ',len(url)+1,' pages to form a loop)\n')
            break

while True:
    page=input("type the page you want to start: ")
    if looptest(page):
        print("Page is not found\n")
