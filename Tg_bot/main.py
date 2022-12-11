import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot("5807155548:AAH54VFkBB43je4jPdgVI68ppISZprU0MIg")
def start(m, res=False):
  markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
  item1=types.KeyboardButton("Картинка")
  markup.add(item1)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'Картинка':
        photo = open('pic/' + random.choice(os.listdir('pic')), 'rb')
        bot.send_photo(message.from_user.id, photo)
bot.polling(none_stop=True, interval=0)