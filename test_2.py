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
    items.pop(i)
    first.append(i)
    break
for m in items:
    m = randrange(0, len(items))
    items.pop(m)
    # items.remove(m)
    second.append(m)
    break
for n in items:
    n = randrange(0, len(items))
    items.pop(n)
    # items.remove(n)
    third.append(n)
    break
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