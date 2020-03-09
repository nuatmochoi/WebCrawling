import requests
from bs4 import BeautifulSoup
import time 
from fake_useragent import UserAgent

ua = UserAgent()

url = "http://c9.inlive.co.kr:6910/"
headers = {'User-Agent' : ua.random}

r = requests.get(url,headers=headers)


bs = BeautifulSoup(r.content.decode('euc-kr','replace'), features="lxml")

t = bs.find_all('font', class_="default")
cnt=0
try:
    for tag in t:
        if cnt == 4:
            listener_text = tag.get_text()
            break
        cnt += 1
    o_index = listener_text.index('o')
    listener = listener_text[30:int(o_index)]
except:
    listener=''

if listener != '':
    result = ' 청취:  ' +listener
else:
    result = ''

print(result)