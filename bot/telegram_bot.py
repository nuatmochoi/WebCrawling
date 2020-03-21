import telegram
import bot_env

bot = telegram.Bot(token = bot_env.token())

# for i in bot.getUpdates():
#     print(i.message)

bot.send_message(chat_id=bot_env.token(), text="테스트입니다.")