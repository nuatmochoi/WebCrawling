from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import requests
import json

url= input("Input youtube url including official music:")
chrome_options= Options()
webdriver_path='C:\\Python37-32\\chromedriver.exe'
ch_driver=webdriver.Chrome(webdriver_path)

ele = ch_driver.find_element_by_tag_name("body") 


ch_driver.get(url)
time.sleep(2)
ch_driver.maximize_window()


ch_driver.find_element_by_id('more').click()
ch_driver.execute_script("window.scrollTo(0,500);")
time.sleep(2)
result=ch_driver.find_element_by_xpath('//*[@id="collapsible"]/ytd-metadata-row-renderer[2]')

song_title=result.text.split('\n')[1]
if '(' in song_title:
    idx=song_title.index('(')
    title=song_title[:idx]
print(title)
ch_driver.quit()
