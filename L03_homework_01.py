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
items = [("PS4 игра Sony Человек-паук", 1349), ("PS4 игра Sony God of War", 1999), ("PS4 игра Sony Detroit: Стать человеком", 1349), ("PS4 игра Sony Одни из нас. Обновленная версия (Хиты PlayStation", 990), ("PS4 игра Sony Uncharted 4: Путь вора (Хиты PlayStation)", 990), ("PS4 игра Sony Дожить до рассвета (Хиты PlayStation)", 990), ("PS4 игра Sony Знание - сила: Эпохи", 690), ("PS4 игра Sony Gran Turismo Sport", 1349), ("PS4 игра Sony Жизнь После", 2590), ("PS4 игра Sony ASTRO BOT Rescue Mission (только для PS VR)", 1340), ("PS4 игра Sony Gravity Rush 2", 1340)]
balance = 5000
my_shop_list = []
total_cost = 0
# Ваш код ниже
first = 'номер первой выбранной игры (индекс)'
second = 'номер второй выбранной игры (индекс)'
third = 'номер третьей выбранной игры (индекс)'
