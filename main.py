from telegram import Bot

bot = Bot('5128554563:AAFAxYqhCb4w5eKXuh5P3iU23apTrLyRz5Q')
print(bot.getMe())
x = bot.getUpdates()
print(x.message.text)