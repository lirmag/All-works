import telebot
import datetime
import schedule
import time
from telebot import types
from datetime import datetime
bot = telebot.TeleBot("5077196358:AAEomf8gyWkr0j7WN10SUGhanyVkPvtIF3s",parse_mode=None) #Токен
status = True
def counting_time_1stream(mnt): #Высчитать статус урока для первого потока
    maximum = 886
    func = 'working'
    lessons_end = {510: 550,
                   525: 565,
                   585: 625,
                   635: 675,
                   685: 725,
                   745: 785,
                   795: 835,
                   845: 885}
    for elem in lessons_end:
        if elem < mnt and lessons_end[elem] > mnt:
            func = 'done'
            return str('The lesson is already in progress!👍')
    if func == 'working':
        for elem in lessons_end:
            if mnt - lessons_end[elem] > 0:
                for el in lessons_end:
                    if mnt > maximum:
                        return str('Lessons are already over!🎉')
                    if mnt < el:
                        if el - mnt == 1:
                            min = ' minute'
                        else:
                            min = ' minutes'
                        ans = str(el - mnt) + min + ' to go before the lesson starts!🕰'
                        return ans
def counting_time_2stream(mnt): #Высчитать статус урока для второго потока
    maximum = 936
    func = 'working'
    lessons_start = {525: 565,
                     575: 615,
                     635: 675,
                     685: 725,
                     735: 775,
                     795: 835,
                     845: 885,
                     895: 935}
    for elem in lessons_start:
        if elem < mnt and lessons_start[elem] > mnt:
            func = 'done'
            return str('The lesson is already in progress!👍')
    if func == 'working':
        for elem in lessons_start:
            if mnt - lessons_start[elem] > 0:
                for el in lessons_start:
                    if mnt > maximum:
                        return str('Lessons are already over!🎉')
                    if mnt < el:
                        if el - mnt == 1:
                            min = ' minute'
                        else:
                            min = ' minutes'
                        ans = str(el - mnt) + min + ' to go before the lesson starts!🕰'
                        return ans
# def send():
#     bot.send_message(message.chat.id,'2 урок начнется через 10 минут!')
        # schedule.every().day.at('18:02').do(bot.send_message(mssage.chat.id, '1 урок начался! Удачного дня!')).tag(
        #     'alerts')
        # schedule.every().day.at('17:58').do(bot.send_message(mssage.chat.id, '2 урок начнется через 10 минут!')).tag(
        #     'alerts')
        # schedule.every().day.at('10:15').do(bot.send_message(message.chat.id, '3 урок начнется через 20 минут!')).tag(
        #     'alerts')
        # schedule.every().day.at('11:15').do(bot.send_message(message.chat.id, '4 урок начнется через 10 минут!')).tag(
        #     'alerts')
        # schedule.every().day.at('12:05').do(bot.send_message(message.chat.id, '5 урок начнется через 10 минут!')).tag(
        #     'alerts')
        # schedule.every().day.at('12:55').do(bot.send_message(message.chat.id, '6 урок начнется через 20 минут!')).tag(
        #     'alerts')
        # schedule.every().day.at('13:55').do(bot.send_message(message.chat.id, '7 урок начнется через 10 минут!')).tag(
        #     'alerts')
        # schedule.every().day.at('14:45').do(bot.send_message(message.chat.id, '8 урок начнется через 10 минут!')).tag(
        #     'alerts')
        # time.sleep(1)
@bot.message_handler(commands=['start'])
def hello(message):
    sti = open('C:/Users/isaev/Desktop/telegram/pictures/hi.tgs', 'rb')
    bot.send_animation(message.chat.id, sti) #Приветственный стикер
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #Начальная клавиатура
    item1 = types.KeyboardButton('Уведомления об уроках🕐')
    item2 = types.KeyboardButton('Call timetable📖')
    item3 = types.KeyboardButton('Status of the lesson✨')
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id, 'Hello, {0.first_name}! What are you interested in?🤔'.format(message.from_user, bot.get_me()), reply_markup=markup) #Поздороваться обязательно
@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        if message.text == 'Уведомления об уроках🕐':
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            it1 = types.InlineKeyboardButton('Да',callback_data='yes')
            it2 = types.InlineKeyboardButton('Нет',callback_data='no')
            keyboard.add(it1,it2)
            bot.send_message(message.chat.id,'Вы уверены,что хотите получать уведомления?',reply_markup=keyboard) #Текущая дата(пробовал функционал)
        elif message.text == 'Call timetable📖':
            markup = types.InlineKeyboardMarkup(row_width=2) #Маленькая клавиатура
            item1 = types.InlineKeyboardButton('1️⃣',callback_data='first')
            item2 = types.InlineKeyboardButton('2️⃣',callback_data='second')
            markup.add(item1,item2)
            bot.send_message(message.chat.id,'No problem! Which stream are you from?💧',reply_markup=markup)
        elif message.text == 'Status of the lesson✨':
            # bot.send_message(message.chat.id, 'Great! Which stream are you from?')
            markup1 = types.InlineKeyboardMarkup(row_width=2)  # Маленькая клавиатура
            item12 = types.InlineKeyboardButton('1️⃣', callback_data='frst')
            item21 = types.InlineKeyboardButton('2️⃣', callback_data='scnd')
            markup1.add(item12, item21)
            bot.send_message(message.chat.id,'Which stream are you from?💧',reply_markup=markup1)
            # bot.send_message(message.chat.id,'Хотите автоматически получать уведомления?')
        else:
            bot.send_message(message.chat.id, 'Sorry, I cant help you😔') #В случае ошибки
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call): #Для маленькой клавиатуры
    try:
        if call.message:
            if call.data == 'first':
                pic_1 = open('C:/Users/isaev/Desktop/telegram/pictures/1potok.jpg','rb') #Фотка первого потока
                bot.send_message(call.message.chat.id,'Here is the bell schedule for stream 1📚:')
                bot.send_photo(call.message.chat.id,pic_1)
            if call.data == 'second':
                pic_2 = open('C:/Users/isaev/Desktop/telegram/pictures/2potok.jpg','rb') #Фотка второго потока
                bot.send_message(call.message.chat.id,'Here is the bell schedule for stream 2📚:')
                bot.send_photo(call.message.chat.id, pic_2)
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Call timetable📖',
            #                       reply_markup=None) #Удаление маленькой клавиатуры
            if call.data == 'frst':
                now = str(datetime.now())
                hrs = int(now[11:13])
                mnt = int(now[14:16])
                mnt += hrs * 60
                bot.send_message(call.message.chat.id, counting_time_1stream(mnt))
            if call.data == 'scnd':
                now = str(datetime.now())
                hrs = int(now[11:13])
                mnt = int(now[14:16])
                mnt += hrs * 60
                bot.send_message(call.message.chat.id, counting_time_2stream(mnt))
            if call.data == 'yes':
                bot.send_message(call.message.chat.id,'Отлично! Бот будет уведомлять вас о начале/конце урока!(для остановки отправьте 1)')
                while True:
                    schedule.every().day.at('18:58').do(bot.send_message(call.message.chat.id, '2 урок начнется через 10 минут!'))
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                       text='Status of the lesson', reply_markup=None)
    except Exception as e:
        print(repr(e))
# if status == True:
#     send()
# @bot.message_handler(content_types=['text'])
# def msg(text):
#     if text.text != '1':
#         schedule.clear('alerts')
# schedule.every().day.at('17:44').do(bot.send_message(text.chat.id, '1 урок начался! Удачного дня!')).tag('alerts')
# schedule.every().day.at('17:45').do(bot.send_message(text.chat.id, '2 урок начнется через 10 минут!')).tag('alerts')
# schedule.every().day.at('10:15').do(bot.send_message(text.chat.id, '3 урок начнется через 20 минут!')).tag('alerts')
# schedule.every().day.at('11:15').do(bot.send_message(text.chat.id, '4 урок начнется через 10 минут!')).tag('alerts')
# schedule.every().day.at('12:05').do(bot.send_message(text.chat.id, '5 урок начнется через 10 минут!')).tag('alerts')
# schedule.every().day.at('12:55').do(bot.send_message(text.chat.id, '6 урок начнется через 20 минут!')).tag('alerts')
# schedule.every().day.at('13:55').do(bot.send_message(text.chat.id, '7 урок начнется через 10 минут!')).tag('alerts')
# schedule.every().day.at('14:45').do(bot.send_message(text.chat.id, '8 урок начнется через 10 минут!')).tag('alerts')
bot.infinity_polling() #Запуск бота