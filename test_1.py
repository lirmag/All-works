<<<<<<< HEAD
import random

items = [("PS4 игра Sony Человек-паук", 1349), ("PS4 игра Sony God of War", 1999),
         ("PS4 игра Sony Detroit: Стать человеком", 1349),
         ("PS4 игра Sony Одни из нас. Обновленная версия (Хиты PlayStation", 990),
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


def zalupa_1():
    while my_shop_list[2] == my_shop_list[1] or my_shop_list[2] == my_shop_list[0] or my_shop_list[1] == my_shop_list[0]:
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
balance -= my_shop_list[2][1]
while balance < 0:
    my_shop_list.append(random.choice(items))
    zalupa_1()
total_cost += my_shop_list[2][1]
first = items.index(my_shop_list[0])
second = items.index(my_shop_list[1])
third = items.index(my_shop_list[2])

one = list(my_shop_list[0])
one.pop(1)
# one = tuple(one)
b = list(my_shop_list[1])
b.pop(1)
# b = tuple(b)
c = list(my_shop_list[2])
c.pop(1)
# c = tuple(c)
my_shop_list.clear()
my_shop_list.append(*one)
my_shop_list.append(*b)
my_shop_list.append(*c)
print('Список покупок:', my_shop_list)
print('Номер первой игры:', first)
print('Номер второй игры:', second)
print('Номер третьей игры:', third)
print('Оставшийся баланс:', balance)
print('Общая сумма:', total_cost)


# def zalupa_1():
#     while my_shop_list[2] == my_shop_list[1] or my_shop_list[2] == my_shop_list[0]:
#         my_shop_list[2] = random.choice(items)

# my_shop_list.append(random.choice(items))
#     while my_shop_list[2] == my_shop_list[1] or my_shop_list[2] == my_shop_list[0]:
#         my_shop_list[2] = random.choice(items)
=======
a = list((input().split())
for i in a:
    if type(i) is str:
        type(i) == int
>>>>>>> a6bd5057dc92ef7139ad1c222ec428beb2eeccd0
