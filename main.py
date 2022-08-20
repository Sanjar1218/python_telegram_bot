from telegram import Bot
import os

bot = Bot(os.environ['token'])
x = bot.getMe()
print(x.username)