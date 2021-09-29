import random
from random import randrange
items = [("PS4 игра Sony Человек-паук", 1349), ("PS4 игра Sony God of War", 1999),
         ("PS4 игра Sony Detroit: Стать человеком", 1349),
         ("PS4 игра Sony Одни из нас. Обновленная версия (Хиты PlayStation", 990),
         ("PS4 игра Sony Uncharted 4: Путь вора (Хиты PlayStation)", 990),
         ("PS4 игра Sony Дожить до рассвета (Хиты PlayStation)", 990), ("PS4 игра Sony Знание - сила: Эпохи", 690),
         ("PS4 игра Sony Gran Turismo Sport", 1349), ("PS4 игра Sony Жизнь После", 2590),
         ("PS4 игра Sony ASTRO BOT Rescue Mission (только для PS VR)", 1340), ("PS4 игра Sony Gravity Rush 2", 1340)]
first = []
second = []
third = []
list_1 = []
balance = 5000
my_shop_list = []
total_cost = 0
for i in items:
    i = randrange(0, len(items))
    my_shop_list.append(items[i])
    first.append(i)
    break
for m in items:
    m = randrange(0, len(items))
    my_shop_list.append(items[m])
    # items.remove(m)
    second.append(m)
    break
for n in items:
    n = randrange(0, len(items))
    my_shop_list.append(items[n])
    # items.remove(n)
    third.append(n)
    break
# list_1.pop(1)
# my_shop_list.append(list_1)
# for i in second:
#     if i == first:
#         second == random.choice(items)
# for pi in third:
#     if pi == first or pi == second:
#         third == random.choice(items)
print(items)
print(first)
print(second)
print(third)
print(my_shop_list)
