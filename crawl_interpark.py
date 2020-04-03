import requests
from bs4 import BeautifulSoup
import time 
from fake_useragent import UserAgent

ua = UserAgent()

url = 'http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Fes&tid4=Fes'
headers = {'User-Agent' : ua.random}

r = requests.get(url, headers=headers)
bs = BeautifulSoup(r.content.decode('euc-kr','replace'), features="lxml")

t = bs.find_all('span', class_="fw_bold")

li=[]
for tag in t:
    title = tag.get_text().strip('\n')
    link = 'http://ticket.interpark.com/' + tag.find('a')['href']
    li.append((title, link))

[print(i) for i in li]

# for ele in li:
#     redirect_url = ele[1]
#     print(redirect_url)
#     each_r = requests.get(url, headers=headers)
#     each_bs = BeautifulSoup(r.content.decode('euc-kr','replace'), 'html.parser')
