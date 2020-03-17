import requests
from bs4 import BeautifulSoup
import time 
from fake_useragent import UserAgent

ua = UserAgent()
url = "http://bh1899.inlive.co.kr/"
headers = {'User-Agent': ua.random}

r = requests.get(url, headers =headers)

bs = BeautifulSoup(r.content.decode('euc-kr', 'replace'), "lxml")

t = bs.find_all('dd', class_="nickname")

for tag in t:
    print(tag.get_text())