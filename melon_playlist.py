import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

ua = UserAgent(verify_ssl=False)

chrome_options = Options()
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
for artist in artists:
    artist_li.append(artist.get_text())

print(artist_li)

ch_driver.quit()