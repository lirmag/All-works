import telebot
import datetime
import sqlite3
import schedule
import config
import time
from telebot import types
from datetime import datetime
bot = telebot.TeleBot(config.TOKEN,parse_mode=None)
@bot.message_handler(commands=['start'])
def hello(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS login_id(id INTEGER)''')

    connect.commit()


    people_id = message.chat.id
    cursor.execute(f'SELECT id FROM login_id WHERE id = {people_id}')
    data = cursor.fetchone()
    if data is None:
        user_id = [message.chat.id]
        cursor.execute('INSERT INTO login_id VALUES(?);',user_id)
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Done')



bot.infinity_polling()