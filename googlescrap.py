import urllib
import urllib.parse
import requests
from bs4 import BeautifulSoup
import re
link=[]
def teks(soup):
    results = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            linkf = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": linkf
            }
            results.append(item)
    return results

def get_page(resp):
    simpan=[]
    URL = f"https://google.com{resp}"
    URL=URL.replace("amp;","&")
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        simpan.append(teks(soup))
    return simpan
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

query = "site:binadarma.ac.id"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    link.append(teks(soup))

    biji=[]
    for g in soup.find_all('td'):
            m=g.find_all('a',class_='fl')
            if(m):
                dl=str(m[0]).split("\"")
                biji.append(dl[5])
    for i in link:
        for g in i:
            print(g['title'])
    for i in biji:
        p=get_page(i)
        for i in p:
                for g in i:
                    print(g['title'])
