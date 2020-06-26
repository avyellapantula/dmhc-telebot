#!/usr/bin/python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import logging
import os


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url


def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def start(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id,
                    text='Hello, Friend! I am a mental health check bot, that also provides you with random pupper pics! /bop for pupper pics and /checkup for basic qs. Type /help to get this message but formatted better plus my hopes and dreams'
                    )


def help(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.sendMessage(chat_id=chat_id,
                    text="Hello, Friend! I am a mental health check bot, that also provides you with random pupper pics! These are very basic questions, just to keep a check or tally on you each day. \n - /bop for pupper pics \n - /checkup for basic qs \n - /help to get this message \n I promised you my hopes and dreams for this bot so here they are. I would like to aggregate the polling data so you know how many times you checked in, and did things, and keep a reminder to not answer the questions more than once in one day. :)")


def checkup(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.sendPoll(chat_id=chat_id,
                 question='Did you do the following today?',
                 options=['Brush your teeth', 'Shower', 'Comb your hair'
                 ], allows_multiple_answers=True, open_period=100)


def main():
    updater = Updater('1032560639:AAG2tRwA60HFiAl4OAOXIcXpyLPapc-4eL0')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    dp.add_handler(CommandHandler('checkup', checkup))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
	
	# for the webhook/heroku thing
	# Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://salty-scrubland-44546.herokuapp.com/' + '1032560639:AAG2tRwA60HFiAl4OAOXIcXpyLPapc-4eL0')

	

if __name__ == '__main__':
    main()
