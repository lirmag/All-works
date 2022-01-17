import telebot
import datetime
from telebot import types
from datetime import datetime
bot = telebot.TeleBot("5077196358:AAEomf8gyWkr0j7WN10SUGhanyVkPvtIF3s",parse_mode=None) #Токен
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
@bot.message_handler(commands=['start'])
def hello(message):
    sti = open('C:/Users/isaev/Desktop/telegram/pictures/hi.tgs', 'rb')
    bot.send_animation(message.chat.id, sti) #Приветственный стикер
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #Начальная клавиатура
    item1 = types.KeyboardButton('Current time🕐')
    item2 = types.KeyboardButton('Call timetable📖')
    item3 = types.KeyboardButton('Status of the lesson✨')
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id, 'Hello, {0.first_name}! What are you interested in?🤔'.format(message.from_user, bot.get_me()), reply_markup=markup) #Поздороваться обязательно
@bot.message_handler(content_types=['text'])
def text(message):
    now = datetime.now()
    if message.chat.type == 'private':
        if message.text == 'Current time🕐':
            bot.send_message(message.chat.id,str(now.strftime("%d-%m-%Y %H:%M"))) #Текущая дата(пробовал функционал)
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
        else:
            bot.send_message(message.chat.id, 'Sorry, I cant help you😔') #В случае ошибки
#
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call): #Для маленькой клавиатуры
    try:
        if call.message:
            if call.data == 'first':
                pic_1 = open('C:/Users/isaev/Desktop/telegram/pictures/1potok.jpg', 'rb') #Фотка первого потока
                bot.send_message(call.message.chat.id,'Here is the bell schedule for stream 1📚:')
                bot.send_photo(call.message.chat.id,pic_1)
            if call.data == 'second':
                pic_2 = open('C:/Users/isaev/Desktop/telegram/pictures/2potok.jpg', 'rb') #Фотка второго потока
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
            # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
            #                       text='Status of the lesson', reply_markup=None)
    except Exception as e:
        print(repr(e))

bot.infinity_polling() #Запуск бота