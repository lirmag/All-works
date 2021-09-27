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
for i in items:
    while total_cost <= 5000:
        i = random.choice(items)
        if type(i) in (int, float):
            my_shop_list += i
            my_shop_list.append(i)
        else:
            my_shop_list.append(i)
print(my_shop_list)
