#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import datetime
import logging
import random

from telegram import Sticker
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from UserInfo import UserInfo

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# глобальные переменные

# словарь id пользователя - информация
users = {}


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    uid = update.message.from_user.id
    uname = update.message.from_user.first_name
    if (uid in users):
        update.message.reply_text('Второй раз не здороваюсь, вспоминай, что я говорила!!!11!11!!')
    else:
        users[uid] = UserInfo(uid)
        users[uid].meetDate = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
        update.message.reply_text(
            'Привет! Я - Гидролиза. Это как Алиса, только тихая. Со мной можно попробовать поболтать, но будьте осторожны: всё, что вы скажете может быть использовано против вас. Если вдруг мне что-то не понравится - я могу перестать разговаривать или начать жужжать. Это значит, ты делаешь что-то неправильно. Я всё сказала, начинай.')
    logger.warning('Пользователь ' + uname + '(' + str(uid) + ') команда: start')


def help(bot, update):
    """Send a message when the command /help is issued."""
    uid = update.message.from_user.id
    uname = update.message.from_user.first_name
    update.message.reply_text('Да ты же тупой, это бесполезно! Разбирайся сам, не беси меня')
    logger.warning('Пользователь ' + uname + '(' + str(uid) + ') команда: help')


def echo(bot, update):
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    count = round(random.random() * 35)
    stri = "ж"
    for number in range(count):
        if random.random() < 0.5:
            stri += "ж"
        else:
            stri += "Ж"
    update.message.reply_text(stri)


def send_stickerpack(bot, update):
    """отправить стикерпак пользователю"""
    uid = update.message.from_user.id
    uname = update.message.from_user.first_name
    update.message.reply_text('СТИКЕРЫЫЫЫ. ща отправлю тебе тоже')
    ans = Sticker("AAQCABPFX-MNAATJAeOoY2ZYLm94AAIC", 256, 256)
    update.message.reply_sticker(ans)
    logger.warning('Пользователь ' + uname + '(' + str(uid) + ') команда: send_stickerpack')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("728805432:AAEginEOKVBEBGExhOPYlvzcY1cFZF9645k")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    # dp.add_handler(CommandHandler("sum", sum))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))  # ответ на текстовое сообщение
    dp.add_handler(MessageHandler(Filters.sticker, send_stickerpack))  # отправка стикеров

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
