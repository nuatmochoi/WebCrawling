import requests
from bs4 import BeautifulSoup
import time 
from fake_useragent import UserAgent

ua = UserAgent()
pre_title='temp'
while(True):
    url = "http://www.inlive.co.kr/search/search.htm?keyword=%B3%BB%B8%E9%C0%B8%B7%CE%C0%C7+%C3%CA%B4%EB"
    headers = {'User-Agent' : ua.random}

    r=requests.get(url)
    bs =BeautifulSoup(r.content.decode('euc-kr','replace'), "html.parser")

    t= bs.find_all('span', class_="music_name")
    title=t[0].get_text()
    if pre_title == title:
        pass
        print("nothing")
    else:
        html_file = open('title.html', 'w', encoding='utf-16')
        html_file.write(title)
        html_file.close()
        print(title)

    pre_title=title
    time.sleep(5)
