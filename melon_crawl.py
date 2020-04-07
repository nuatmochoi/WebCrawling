from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import getpass
import time

ua = UserAgent(verify_ssl=False)
userAgent = ua.random

chrome_options = Options()
#chrome_options.add_argument('headless')
#chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument(f'user-agent={userAgent}')

webdriver_path = 'C:\\Python37-32\\chromedriver.exe'
ch_driver = webdriver.Chrome(webdriver_path, chrome_options=chrome_options)

url = "https://accounts.kakao.com/login?continue=https%3A%2F%2Fkauth.kakao.com%2Foauth%2Fauthorize%3Fclient_id%3D6cfb479f221a5adc670fe301e1b6690c%26redirect_uri%3Dhttps%253A%252F%252Fmember.melon.com%252Foauth.htm%26response_type%3Dcode%26state%3DmKzaPWr6tQ%2540OGJOvAySTa0VYbkHj2l7%252Fc5G51Jlz5XU1V%2540OzzBKHmE3v84%2540iWoSqz7TNWSz8z05%252Fa8wFLlPj4A%253D%253D%26encode_state%3Dtrue"

ch_driver.get(url)
ch_driver.maximize_window()
kakao_id = ch_driver.find_element_by_xpath('//*[@id="id_email_2"]')
kakao_pw = ch_driver.find_element_by_xpath('//*[@id="id_password_3"]')

str_id = input()
str_pw = getpass.getpass('input password: ')

kakao_id.send_keys(str_id)
kakao_pw.send_keys(str_pw)

ch_driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button').click()
time.sleep(3)

ch_driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[2]/li[1]/a').click()
time.sleep(3)
ch_driver.find_element_by_xpath('//*[@id="conts"]/div[1]/ul/li[4]/a').click()


time.sleep(3)
ch_driver.quit()