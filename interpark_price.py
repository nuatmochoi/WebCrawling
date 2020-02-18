import requests, re, json

# Just a random product url, you can adapt the code into yours.
url = "http://ticket.interpark.com/Ticket/Goods/GoodsInfo.asp?GroupCode=20002746"

data = requests.get(url).text

# I used regex to get the matching values `vGC` and `vPC`
vGC = re.search(r"var vGC = \"(\d+)\"", data).groups()[0]
vPC = re.search(r"var vPC = \"(\d+)\"", data).groups()[0]

# Notice that I placed placeholders to use `format`. Placeholders are `{}`.
priceUrl = "http://ticket.interpark.com/Ticket/Goods/GoodsInfoJSON.asp?Flag=SalesPrice&GoodsCode={}&PlaceCode={}"

# Looks like that url needs a referer url and that is the goods page, we will pass it as header.
lastData = requests.get(priceUrl.format(vGC, vPC), headers={"Referer": url}).text

# As the data is a javascript object but inside it is a json object,
# we can remove the callback and parse the inside of callback as json data:
lastData = re.search(r"^Callback\((.*)\);$", lastData).groups()[0]
lastData = json.loads(lastData)["JSON"]

print(lastData)
