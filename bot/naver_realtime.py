import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import telegram
import bot_env
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = bot_env.token())
ua = UserAgent()
headers = {'User-Agent': ua.random}
url = "https://datalab.naver.com/keyword/realtimeList.naver?where=main"

def job_function():
    msg =""
    html = requests.get(url, headers=headers)
    bs = BeautifulSoup(html.text, "html.parser")
    t = bs.find_all("span", class_ ="item_title")
    for tag in t:
        msg=msg+tag.text+"\n"
    bot.send_message(chat_id=bot_env.id(), text=msg)
    sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30, id="job1")
sched.start()