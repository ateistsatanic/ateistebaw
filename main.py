import config
import telebot
import random

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('bot/sticker.webm', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send.message(message.chat.id, "ебем твою мать")


@bot.message_handler(commands=['ateist'])
def spam(message):
    sti = open('bot/sticker.webm', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.respond.message(message.chat.id, random.choice(shabl))
