# -*- coding: utf-8 -*-
"""
1. Создайте функцию gift_to_people так, чтобы она использовала в качестве аргументов две переменные, в которые мы будем передавать <имя человека> и <подарок>, а сообщение будет иметь вид:
«Добрый день, <имя человека>!»
«В подарок вы получаете <подарок>!»
2. Вызовите функцию gift_to_people, используя позиционные аргументы: для имени человека - укажите свое имя; для подарка - любой подарок
3. Вызовите функцию gift_to_people, используя именованные аргументы: для имени человека - укажите имя своего друга;  для подарка - любой подарок
4. Создайте функцию sum_two_number, которая принимает в качестве аргумента любые два числа и выводит на экран сумму этих чисел
"""


# Ваш код ниже
def gift_to_people(name, gift):
    print('Добрый день, ' + name + '!')
    print('В подарок вы получаете ' + gift + '!')


gift_to_people('Лиза', 'резиновый член')
gift_to_people('Илья', 'свою мёртвую мать')


def sum_two_number(number_1, number_2):
    print(number_2 + number_1)


sum_two_number(2, 10)