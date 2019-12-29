import requests
from bs4 import BeautifulSoup

tomato_uri = "http://www.rottentomatoes.com/"
response = requests.get(tomato_uri)
response

html = response.text
html[:400]

bs =BeautifulSoup(html, "html.parser")

tag=bs.find_all('div',id='homepage-top-box-office')[0].find_all('td',"middle_col")
for td in tag:
    print(td.get_text().strip('\n'))
