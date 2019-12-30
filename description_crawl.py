from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


chrome_options= Options()
webdriver_path='C:\\Python\\chromedriver.exe'
ch_driver=webdriver.Chrome(webdriver_path)
ch_driver.get('https://www.youtube.com')
ch_driver.maximize_window()
time.sleep(1)
ch_driver.find_element_by_xpath('//*[@id="video-title-link"]').click()

for _ in range(5):
    try:
        element=WebDriverWait(ch_driver,20).until(
            EC.presence_of_element_located((By.ID,'thumbnail'))
        )
        time.sleep(1.5)
        description=ch_driver.find_element_by_xpath('//*[@id="description"]/yt-formatted-string')
        print(description.text)
        next_xpath=ch_driver.find_element_by_xpath('//*[@id="dismissable"]/div/div[1]/a')
        ch_driver.execute_script("arguments[0].click();",next_xpath) 
    except TimeoutError:
        print("Page did not open within 10 seconds, or there was no tag for xpath.")
    finally:
        pass
ch_driver.quit()
    
