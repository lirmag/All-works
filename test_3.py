import random
from random import randrange
items = [("PS4 игра Sony Человек-паук", 1349), ("PS4 игра Sony God of War", 1999),
         ("PS4 игра Sony Detroit: Стать человеком", 1349),
         ("PS4 игра Sony Одни из нас. Обновленная версия (Хиты PlayStation", 990)]
first = []
second = []
third = []
balance = 5000
my_shop_list = []
total_cost = 0
for i in items:
    i = randrange(0, len(items))
    my_shop_list.append(items[i])
    items.pop(i)
    first.append(i)
    break
for m in items:
    m = randrange(0, len(items))
    my_shop_list.append(items[m])
    items.pop(m)
    # items.remove(m)
    second.append(m)
    break
for n in items:
    n = randrange(0, len(items))
    my_shop_list.append(items[n])
    items.pop(n)
    # items.remove(n)
    third.append(n)
    break
print(items)
print(first)
print(second)
print(third)
print(my_shop_list)