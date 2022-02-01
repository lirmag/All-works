import telebot
import datetime
bot = telebot.TeleBot("5077196358:AAEomf8gyWkr0j7WN10SUGhanyVkPvtIF3s",parse_mode=None)
@bot.message_handler(commands=['start'])
def hello(message):
    sticker = open('telegram/hello/hello.webp')
    bot.send_sticker(message.chat.id,sticker)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>.'.format(message.from_user, bot.get_me()),parse_mode='html')
@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id,message.text)

bot.polling(none_stop=True)