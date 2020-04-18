import requests
from bs4 import BeautifulSoup
import time 
from fake_useragent import UserAgent

ua = UserAgent()
whole_concert_url = 'http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&Sort=1'
url = 'http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Fes&tid4=Fes'

headers = {'User-Agent' : ua.random}

r = requests.get(whole_concert_url, headers=headers)
bs = BeautifulSoup(r.content.decode('euc-kr','replace'), features="lxml")

t = bs.find_all('span', class_="fw_bold")
loc_t = bs.find_all('td', class_="Rkdate")

loc_li = []
for tag in loc_t:
        location = tag.get_text().strip('\n')
        loc_li.append(location)

li=[]
for tag in t:
    title = tag.get_text().strip('\n')
    link = 'http://ticket.interpark.com/' + tag.find('a')['href']

    li.append((title, link))

[print(i) for i in loc_li]

# for ele in li:
#     redirect_url = ele[1]
#     print(redirect_url)
#     each_r = requests.get(url, headers=headers)
#     each_bs = BeautifulSoup(r.content.decode('euc-kr','replace'), 'html.parser')
