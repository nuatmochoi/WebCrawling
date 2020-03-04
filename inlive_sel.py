# -*- coding:utf-16 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options= Options()
chrome_options.add_argument('headless')
#chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

webdriver_path='C:\\Python37-32\\chromedriver.exe'
ch_driver=webdriver.Chrome(webdriver_path, chrome_options=chrome_options)
ch_driver.get('http://www.inlive.co.kr/webplayer/index.htm?f_bsid=c5145&t=12034194118')

time.sleep(0.5)
title=ch_driver.find_element_by_class_name('table_title')
text= title.text.encode('utf-16').strip().decode('utf-16')
print(text)
html_file = open('title.html', 'w', encoding='utf-16')
html_file.write(text)
html_file.close()

ch_driver.quit()
    
