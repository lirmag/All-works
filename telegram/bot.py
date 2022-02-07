import telebot7
import datetime
from telebot import types
from datetime import datetime

bot = telebot.TeleBot("5077196358:AAEomf8gyWkr0j7WN10SUGhanyVkPvtIF3s", parse_mode=None)  # Токен


@bot.message_handler(commands=['start'])
def hello(message):
    sti = open('C:/Users/isaev/Desktop/telegram/pictures/hi.tgs', 'rb')
    bot.send_animation(message.chat.id, sti)  # Приветственный стикер
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Начальная клавиатура
    item1 = types.KeyboardButton('Текущее время🕐')
    item2 = types.KeyboardButton('Расписание звонков📖')
    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}✋! Что хотите узнать?'.format(message.from_user, bot.get_me()),
                     reply_markup=markup)  # Поздороваться обязательно


@bot.message_handler(content_types=['text'])
def text(message):
    now = datetime.now()
    if message.chat.type == 'private':
        if message.text == 'Текущее время🕐':
            bot.send_message(message.chat.id, str(now.strftime("%d-%m-%Y %H:%M")))  # Текущая дата(пробовал функционал)
        elif message.text == 'Расписание звонков📖':
            markup = types.InlineKeyboardMarkup(row_width=2)  # Маленькая клавиатура
            item1 = types.InlineKeyboardButton('1️⃣', callback_data='first')
            item2 = types.InlineKeyboardButton('2️⃣', callback_data='second')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Без проблем! Из какого ты потока?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Ничем не могу помочь😔')  # В случае ошибки


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):  # Для маленькой клавиатуры
    try:
        if call.message:
            if call.data == 'first':
                pic_1 = open('C:/Users/isaev/Desktop/telegram/pictures/1potok.jpg', 'rb')  # Фотка первого потока
                bot.send_message(call.message.chat.id, 'Вот расписание звонков для 1 потока📚:')
                bot.send_photo(call.message.chat.id, pic_1)
            if call.data == 'second':
                pic_2 = open('C:/Users/isaev/Desktop/telegram/pictures/2potok.jpg', 'rb')  # Фотка второго потока
                bot.send_message(call.message.chat.id, 'Вот раписание звонков для 2 потока📚:')
                bot.send_photo(call.message.chat.id, pic_2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='Раписание звонков',
                                  reply_markup=None)  # Удаление маленькой клавиатуры
    except Exception as e:
        print(repr(e))


bot.infinity_polling()  # Запуск бота
