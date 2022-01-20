import telebot
import datetime
import sqlite3
import schedule
import config
import time
from telebot import types
from datetime import datetime

bot = telebot.TeleBot(config.TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def hello(message):
    # Keyboard
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Хочу получать уведомления🔔')
    item2 = types.KeyboardButton('Нет,спасибо😒')
    item3 = types.KeyboardButton('Расписание звонков🕧')
    keyboard.add(item1, item2, item3)

    # Welcome(animation)
    sti = open('C:/Users/isaev/Desktop/telegram/pictures/hi.tgs', 'rb')
    bot.send_message(message.chat.id, 'Привет, {0.first_name}, хотите получать уведомления об уроках '
                                      'или посмотреть расписание звонков?🤔'.format(message.from_user, bot.get_me()),
                     reply_markup=keyboard)
    bot.send_animation(message.chat.id, sti)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.chat.type == 'private':

        if message.text == 'Хочу получать уведомления🔔':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('1️⃣')
            item2 = types.KeyboardButton('2️⃣')
            keyboard.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично! Из какого ты потока?', reply_markup=keyboard)

        if message.text == 'Нет,спасибо😒':
            bot.send_message(message.chat.id,
                             'Дайте знать,если захотите включить уведомления или посмотреть расписание звонков!😉')

        if message.text == 'Расписание звонков🕧':
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('1️⃣💧')
            item2 = types.KeyboardButton('2️⃣💧')
            keyboard.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, из какого ты потока?', reply_markup=keyboard)

        if message.text == '1️⃣💧':
            pic_2 = open('C:/Users/isaev/Desktop/telegram/pictures/1potok.jpg', 'rb')
            bot.send_message(message.chat.id, 'Вот расписание звонков для 1️⃣ потока 📚:')
            bot.send_photo(message.chat.id, pic_2)
            bot.send_message(message.chat.id, 'Удачного дня!🍀')

        if message.text == '2️⃣💧':
            pic_2 = open('C:/Users/isaev/Desktop/telegram/pictures/2potok.jpg', 'rb')
            bot.send_message(message.chat.id, 'Вот расписание звонков для 2️⃣ потока 📚:')
            bot.send_photo(message.chat.id, pic_2)
            bot.send_message(message.chat.id, 'Удачного дня!🍀')

        if message.text == '1️⃣':

            keyboard_stop_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('🛑')
            keyboard_stop_1.add(item1)

            bot.send_message(message.chat.id, 'Уведомления об уроках для 1️⃣ потока включены! '
                                              'Если ты захочешь остановить рассылку, то нажми на кнопку 🛑',
                             reply_markup=keyboard_stop_1)

            # connect DB and create the table
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS login_id(id INTEGER)''')
            connect.commit()

            # check ID in the fields
            people_id = message.chat.id
            cursor.execute(f'SELECT id FROM login_id WHERE id = {people_id}')
            data = cursor.fetchone()
            if data is None:
                # add values in the fields
                user_id = [message.chat.id]
                cursor.execute('INSERT INTO login_id VALUES(?);', user_id)
                connect.commit()

            # Unpacking SQL DB
            for value in cursor.execute("SELECT * FROM login_id"):
                schedule.every().day.at('08:30').do(bot.send_message, value[0], '1 урок начался! Удачного дня!').tag(
                    'alert')

                schedule.every().day.at('09:10').do(bot.send_message, value[0], '2 урок начнется через 15 минут!').tag(
                    'alert')

                schedule.every().day.at('10:05').do(bot.send_message, value[0], '3 урок начнется через 10 минут!').tag(
                    'alert')

                schedule.every().day.at('10:55').do(bot.send_message, value[0], '4 урок начнется через 20 минут!').tag(
                    'alert')

                schedule.every().day.at('11:55').do(bot.send_message, value[0], '5 урок начнется через 10 минут!').tag(
                    'alert')

                schedule.every().day.at('12:45').do(bot.send_message, value[0], '6 урок начнется через 10 минут!').tag(
                    'alert')

                schedule.every().day.at('13:35').do(bot.send_message, value[0], '7 урок начнется через 20 минут!').tag(
                    'alert')

                schedule.every(1).seconds.do(bot.send_message, value[0], '8 урок начнется через 10 минут!').tag(
                    'alert')
            while message.text != '🛑':
                schedule.run_pending()
                time.sleep(1)

        if message.text == '2️⃣':

            keyboard_start_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('⏹')
            keyboard_start_2.add(item1)

            bot.send_message(message.chat.id, 'Уведомления об уроках для 2️⃣ потока включены! '
                                              'Если ты захочешь остановить рассылку, то нажми на кнопку ⏹',
                             reply_markup=keyboard_start_2)

            # connect DB and create the table
            connect = sqlite3.connect('users.db')
            cursor = connect.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS login_id(id INTEGER)''')
            connect.commit()

            # check ID in the fields
            people_id = message.chat.id
            cursor.execute(f'SELECT id FROM login_id WHERE id = {people_id}')
            data = cursor.fetchone()
            if data is None:
                # add values in the fields
                user_id = [message.chat.id]
                cursor.execute('INSERT INTO login_id VALUES(?);', user_id)
                connect.commit()

            # Unpacking SQL DB
            for value in cursor.execute("SELECT * FROM login_id"):
                schedule.every().day.at('08:45').do(bot.send_message, value[0], '1 урок начался! Удачного дня!').tag(
                    'alerts')

                schedule.every().day.at('09:25').do(bot.send_message, value[0], '2 урок начнется через 10 минут!').tag(
                    'alerts')

                schedule.every().day.at('10:15').do(bot.send_message, value[0], '3 урок начнется через 20 минут!').tag(
                    'alerts')

                schedule.every().day.at('11:15').do(bot.send_message, value[0], '4 урок начнется через 10 минут!').tag(
                    'alerts')

                schedule.every().day.at('12:05').do(bot.send_message, value[0], '5 урок начнется через 10 минут!').tag(
                    'alerts')

                schedule.every().day.at('12:55').do(bot.send_message, value[0], '6 урок начнется через 20 минут!').tag(
                    'alerts')

                schedule.every().day.at('13:55').do(bot.send_message, value[0], '7 урок начнется через 10 минут!').tag(
                    'alerts')

                schedule.every(1).seconds.do(bot.send_message, value[0], '8 урок начнется через 10 минут!').tag(
                    'alerts')

        if message.text == '🛑':
            schedule.clear('alert')
            bot.send_message(message.chat.id, 'Рассылка уведомлений остановлена!')

            keyboard_stop_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Хочу получать уведомления🔔')
            item2 = types.KeyboardButton('Нет,спасибо😒')
            item3 = types.KeyboardButton('Расписание звонков🕧')
            keyboard_stop_1.add(item1, item2, item3)

            bot.send_message(message.chat.id,
                             'Дайте знать,если снова захотите включить уведомления🔔 или посмотреть расписание звонков!🕧',
                             reply_markup=keyboard_stop_1)

        if message.text == '⏹':
            schedule.clear('alerts')
            bot.send_message(message.chat.id, 'Рассылка уведомлений остановлена!')

            keyboard_stop_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Хочу получать уведомления🔔')
            item2 = types.KeyboardButton('Нет,спасибо😒')
            item3 = types.KeyboardButton('Расписание звонков🕧')
            keyboard_stop_2.add(item1, item2, item3)

            bot.send_message(message.chat.id,
                             'Дайте знать,если снова захотите включить уведомления🔔 или посмотреть расписание звонков!🕧',
                             reply_markup=keyboard_stop_2)

        if message.text == '1️⃣💧':
            keyboard_pic1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Хочу получать уведомления🔔')
            item2 = types.KeyboardButton('Нет,спасибо😒')
            item3 = types.KeyboardButton('Расписание звонков🕧')
            keyboard_pic1.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Могу ли я ещё чем-то помочь?🤔', reply_markup=keyboard_pic1)

        if message.text == '2️⃣💧':
            keyboard_pic2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Хочу получать уведомления🔔')
            item2 = types.KeyboardButton('Нет,спасибо😒')
            item3 = types.KeyboardButton('Расписание звонков🕧')
            keyboard_pic2.add(item1, item2, item3)

            bot.send_message(message.chat.id, 'Могу ли я ещё чем-то помочь?🤔', reply_markup=keyboard_pic2)


bot.infinity_polling()