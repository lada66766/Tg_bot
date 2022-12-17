import telebot
import random
import os
from telebot import types

bot = telebot.TeleBot("5807155548:AAH54VFkBB43je4jPdgVI68ppISZprU0MIg")

f = open('name.txt', 'r', encoding='UTF-8')
name = f.read().split('\n')
f.close()
f = open('txtau.txt', 'r', encoding='UTF-8')
audio_js = f.read().split('\n')
f.close()

@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Картинка")
    markup.add(item1)
    item2 = types.KeyboardButton("GIF")
    markup.add(item2)
    bot.send_message(m.chat.id, 'Нажми:\nКартинка, если хочешь узнать какой из 50 Ёожыгов ты сегодня',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'Картинка':
        photo = open('pic/' + random.choice(os.listdir('pic')), 'rb')
        bot.send_photo(message.from_user.id, photo,random.choice(name))
    if message.text.strip() == 'GIF':
        document = open('gif/' + random.choice(os.listdir('gif')), 'rb')
        audio = open('audio/' + random.choice(os.listdir('audio')), 'rb')
        bot.send_photo(message.from_user.id, document)
        bot.send_audio(message.from_user.id, audio)





bot.polling(none_stop=True, interval=0)