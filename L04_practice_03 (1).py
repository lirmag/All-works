# -*- coding: utf-8 -*-
"""
ЧАСТЬ 1.
1. Дан код смайла Эмоджи smile
2. Используя range() и цикл for выведите самйлы от 1 до 7 на строке
    Пример:
😀 
😀 😀
😀 😀 😀 
😀 😀 😀 😀 
😀 😀 😀 😀  😀 
😀 😀 😀 😀 😀  😀  
😀 😀 😀 😀 😀  😀 😀

Часть 2.
1. Используя range() создайте числовой список numbers, состоящий из чисел в диапазоне от 11 до 121 c шагом 11.
2. Дан пустой список square_numbers.
3. Наполните список square_numbers в цикле for числами из полученного списка numbers, на каждое число возведите в квадрат (n ** 2) 
4. Выведите содержимое списка square_numbers на экран.
    Пример:
        содержимое списка square_numbers: [121, 484, 1089, 1936, 3025, 4356, 5929, 7744, 9801, 12100, 14641]
        
"""
print("ЧАСТЬ 1\n")
smile = "\U0001f600"
# Ваш код ниже
smile = "\U0001f600"
for i in range(0,7):
    print(smile * i)
    

print("ЧАСТЬ 2\n")

numbers = list()
square_numbers = []
# Ваш код ниже

print("содержимое списка square_numbers:", square_numbers)

# Часть 1:
smile = "\U0001f600"
for i in range(0,8):
    print(smile * i)
# Часть 2:
square_numbers = []
for i in range(11,122,11):
    i = i ** 2
    square_numbers.append(i)
print("содержимое списка square_numbers:", square_numbers)
