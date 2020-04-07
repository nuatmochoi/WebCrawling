# 로그인 과정에서 캐시나 브라우저에 저장되는 것들에 대한 처리가 필요할까?
# 가수의 괄호 안 내용 처리는 어떻게 하면 좋을까?
# 파이어폭스와 크롬 driver -> 잠재적인 오류 이슈 있는 것으로 기억함
# 잘못된 아이디와 비밀번호로 로그인했을 때 에러처리
# 멜론 최근 감상한 음악에서 2페이지가 크롤링 안되는 이슈

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from fake_useragent import UserAgent
from user_agents import parse
from bs4 import BeautifulSoup
from collections import Counter
import getpass


ua = UserAgent(verify_ssl=False)
while True:
    userAgent = ua.random
    if parse(userAgent).is_tablet == True: # random 단말기가 tablet인 경우 총 3개의 창이 켜지게 되는 것 방지
        continue
    break

# headless mode
chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument('--log-level=3') # headless 모드 사용시 log 미표시

# 사람처럼 보이기 위한 작업
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("lang=ko_KR")   
chrome_options.add_argument(f'user-agent={userAgent}') 

webdriver_path = 'C:\\Python37-32\\chromedriver.exe'
ch_driver = webdriver.Chrome(webdriver_path, chrome_options=chrome_options)

login_url = "https://www.melon.com/index.htm"
ch_driver.get(login_url)

ch_driver.find_element_by_xpath('//*[@id="gnbLoginDiv"]/div/button').click()
ch_driver.find_element_by_xpath('//*[@id="conts_section"]/div/div/div[1]/button').click()
WebDriverWait(ch_driver, 10).until(lambda d: len(d.window_handles) == 2) # window 개수가 2개가 될 때까지 기다림 (카카오로그인 시 창이 2개 뜨기 때문)
ch_driver.switch_to.window(ch_driver.window_handles[1]) # 두번째 창으로 전환

kakao_id = ch_driver.find_element_by_xpath('//*[@id="id_email_2"]')
kakao_pw = ch_driver.find_element_by_xpath('//*[@id="id_password_3"]')

str_id = input("Input ID: ") 
kakao_id.clear()
kakao_id.send_keys(str_id) # 아이디 입력

str_pw = getpass.getpass('Input Password: ')
kakao_pw.clear()
kakao_pw.send_keys(str_pw) # 패스워드 입력

ch_driver.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button').click() # 로그인 버튼 클릭
ch_driver.implicitly_wait(3)
ch_driver.switch_to.window(ch_driver.window_handles[0]) # 원래 창으로 전환

ch_driver.find_element_by_xpath('//*[@id="gnb_menu"]/ul[2]/li[1]/a').click()
ch_driver.implicitly_wait(3)
ch_driver.find_element_by_xpath('//*[@id="conts"]/div[1]/ul/li[4]/a').click()

html = ch_driver.page_source
bs = BeautifulSoup(html, 'html.parser')
artists = bs.select('#artistName > a.fc_mgray')

artist_li = []
for artist in artists:
    artist_li.append(artist.get_text().strip('\n'))

ch_driver.quit()

artist_dict = dict(Counter(artist_li))
frequency = sorted(artist_dict.items(), key = lambda x: x[1], reverse=True)
print(max(frequency, key=lambda x: x[1])[0])