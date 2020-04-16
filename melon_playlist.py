import re
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from user_agents import parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



ua = UserAgent(verify_ssl=False)

while True:
    userAgent = ua.random
    if parse(userAgent).is_mobile == False:
        continue
    break

chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--log-level=3')

chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("lang=ko_KR")   
chrome_options.add_argument(f'user-agent={ua.random}') 

webdriver_path = 'C:\\Python37-32\\chromedriver.exe'
ch_driver = webdriver.Chrome(webdriver_path, chrome_options=chrome_options)

url = 'http://kko.to/hvnCNCR0T'
ch_driver.get(url)
ch_driver.implicitly_wait(3)

html = ch_driver.page_source

bs = BeautifulSoup(html, 'html.parser')
artists = bs.select('#artistName > a.fc_mgray')

artist_li = []
href_li = []
for artist in artists:
    artist_li.append(artist.get_text())
    href_li.append(artist.attrs['href'][0:-2] + ",'2')")

for script in href_li:
    ch_driver.execute_script(script)
    ch_driver.implicitly_wait(3)

    detail = ch_driver.page_source
    bs = BeautifulSoup(detail, 'html.parser')
    artist_infos = bs.findAll('dl', class_='list_define clfix')
    info_str = ''
    for info in artist_infos:
        info_str += str(info)
    genre = re.search(r'(장르</dt>\n<dd>)([^, <]+)', info_str).groups()[1]
    genre = genre.replace('amp;','')
    print(genre)

    ch_driver.back()
    ch_driver.implicitly_wait(2)

    artist_li[]

ch_driver.quit()