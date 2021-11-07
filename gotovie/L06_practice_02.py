# -*- coding: utf-8 -*-
"""
1. Создайте функцию glad_to_see_you, которая будет использовать в качестве аргумента переменную, в которую мы необходимо передавать <имя человека>, а сообщение будет иметь вид:
        «Рады Вас видеть, <имя человека>!»,
2. Вызовите функцию glad_to_see_you три раза.
3. Создайте функцию square_number(),которая принимает в качестве аргумента любое число и выводит его квадрат (**2) на экран.
4. Вызовите функцию square_number() три раза.
"""

# Ваш код ниже
def glad_to_see(name):
    return 'Рады Вас видеть, ' + name + '!'
print(glad_to_see('Лиза'))
print(glad_to_see('Олег'))
print(glad_to_see('Максим'))
def square_number(number):
    return number**2
print(square_number(2))
print(square_number(4))
print(square_number(8))