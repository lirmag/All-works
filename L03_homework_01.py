# -*- coding: utf-8 -*-
"""
SHOPPING
1. Дан список игр доступных для покупки items, элементами которого являются кортежи содержащие два элемента:
    первый элемент - название игры
    второй элемент - стоимость игры
2. Дан баланс (balance), на который Вы можете расчитывать при покупках.
3. Переменная my_shop_list - пустой список.
4. Переменная total_cost - общая стоимость выбранных игр
5. Выберите 3 любых игры (индексы сохраните в переменные first, second, third) из списка items и сохраните только название игры в список my_shop_list, если стоимость игры не превышает ваш баланс (balance)
Имейте ввиду, что баланс должнен уменьшаться после каждой покупки
6. Выведите список покупок my_shop_list  и общую стоимость total_cost на экран и общее количество купленных игр.
"""
items = [("PS4 игра Sony Человек-паук", 1349), ("PS4 игра Sony God of War", 1999),
         ("PS4 игра Sony Detroit: Стать человеком", 1349),
         ("PS4 игра Sony Одни из нас. Обновленная версия (Хиты PlayStation)", 990),
         ("PS4 игра Sony Uncharted 4: Путь вора (Хиты PlayStation)", 990),
         ("PS4 игра Sony Дожить до рассвета (Хиты PlayStation)", 990), ("PS4 игра Sony Знание - сила: Эпохи", 690),
         ("PS4 игра Sony Gran Turismo Sport", 1349), ("PS4 игра Sony Жизнь После", 2590),
         ("PS4 игра Sony ASTRO BOT Rescue Mission (только для PS VR)", 1340), ("PS4 игра Sony Gravity Rush 2", 1340)]
balance = 5000
my_shop_list = []
total_cost = 0
# Ваш код ниже
first = 'номер первой выбранной игры (индекс)'
second = 'номер второй выбранной игры (индекс)'
third = 'номер третьей выбранной игры (индекс)'

import random

def func_2(arg):
    arg = list(my_shop_list[0])
    arg.pop(1)
def func_1():
    while my_shop_list[2] == my_shop_list[1] or my_shop_list[2] == my_shop_list[0]:
        my_shop_list[2] = random.choice(items)


my_shop_list.append(random.choice(items))
balance -= my_shop_list[0][1]
total_cost += my_shop_list[0][1]
my_shop_list.append(random.choice(items))
while my_shop_list[1] == my_shop_list[0]:
    my_shop_list[1] = random.choice(items)
balance -= my_shop_list[1][1]
total_cost += my_shop_list[1][1]
my_shop_list.append(random.choice(items))
func_1()
balance -= my_shop_list[2][1]
while balance < 0:
    my_shop_list.append(random.choice(items))
    func_1()
total_cost += my_shop_list[2][1]
first = items.index(my_shop_list[0])
second = items.index(my_shop_list[1])
third = items.index(my_shop_list[2])

one = list(my_shop_list[0])
one.pop(1)
b = list(my_shop_list[1])
b.pop(1)
c = list(my_shop_list[2])
c.pop(1)
my_shop_list.clear()
my_shop_list.append(*one)
my_shop_list.append(*b)
my_shop_list.append(*c)
print('Список покупок:', (', '.join(map(str, my_shop_list))))
print('номер первой выбранной игры (индекс):', first)
print('номер второй выбранной игры (индекс):', second)
print('номер третьей выбранной игры (индекс):', total_cost)
# print('Оставшийся баланс:', balance)

