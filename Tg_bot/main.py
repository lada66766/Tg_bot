import telebot
import random
import os
from telebot import types

bot = telebot.TeleBot("5807155548:AAH54VFkBB43je4jPdgVI68ppISZprU0MIg")

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Картинка")
    markup.add(item1)
    bot.send_message(m.chat.id, 'Нажми: \nКартинка  Если хочешь узнать какой из 50 Ёожыгов ты сегодня',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'Картинка':
        photo = open('pic/' + random.choice(os.listdir('pic')), 'rb')
        bot.send_photo(message.from_user.id, photo)

bot.polling(none_stop=True, interval=0)