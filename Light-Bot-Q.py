import os

X = os.getenv('X')                     # ADAFRUIT_IO_USERNAME
Y = os.getenv('Y')                     # ADAFRUIT_IO_KEY

from Adafruit_IO import Client, Feed
aio = Client(X,Y)

from telegram.ext import Updater,CommandHandler, MessageHandler, filters  

import requests  # Getting the data from the cloud


def lighton(bot,update):
    data = aio.send('lightbot', 1)
    rdata = aio.receive('lightbot').value
    chat_id = update.message.chat_id
    bot.send_message(chat_id,text='Light is On')


def lightoff(bot,update):
    data = aio.send('lightbot', 0)
    rdata = aio.receive('lightbot').value
    chat_id = update.message.chat_id
    bot.send_message(chat_id,text='Light is Off')
   
   
u = Updater('1364109578:AAEcZrWvdo-DmYeNeWVWOzpZzl_AOSmjP5k')
dp = u.dispatcher


#dp.add_handler(MessageHandler(filters.text , lighton))

dp.add_handler(CommandHandler("on",lighton))
dp.add_handler(CommandHandler("off",lightoff))
u.start_polling()
u.idle()
