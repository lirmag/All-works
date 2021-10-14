# -*- coding: utf-8 -*-
"""
1. Дан список numbers_with_numbers, состоящий из числовых списков.
2. Используя вложенный цикл (nested_loops) выведите на экран все четные числа.
* подсказка: для определения четности числа используйте n % 2 == 0
    Пример:
        2
        -6
        22
        2
        4
        2
"""
# numbers_with_numbers = [[11, 2, -6, 3], [7, 22, -17, 2], [3, 5, 7, 4], [2, -11, -19, 29]]
# Ваш код ниже
# Решение 1:
from itertools import chain
numbers_with_numbers = [[11, 2, -6, 3], [7, 22, -17, 2], [3, 5, 7, 4], [2, -11, -19, 29]]
numbers_with_numbers = list(chain(*numbers_with_numbers))
for i in numbers_with_numbers:
    if i % 2 == 0:
        print(i)
# Решение 2(если сделать попроще и не выпендриваться):
numbers_with_numbers_1 = []
numbers_with_numbers = [[11, 2, -6, 3], [7, 22, -17, 2], [3, 5, 7, 4], [2, -11, -19, 29]]
for i in numbers_with_numbers:
    for j in i:
        numbers_with_numbers_1.append(j)
for i in numbers_with_numbers_1:
    if i % 2 == 0:
        print(i)
