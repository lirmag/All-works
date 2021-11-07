# -*- coding: utf-8 -*-
"""
1. Напишите функцию count_word_len(), которая будет принимать в качестве аргумента список слов и возвращать словарь, в котором ключ - слово из списка, значение - количество букв в слове. 
"""

# Ваш код ниже
list_1 = ['dog','cat','bee','fish','mouse']
def count_word_len(sp):
    d = dict()
    for element in sp:
        if element not in d:
            d[element] = len(element)
        else:
            continue
    return d
print(count_word_len(list_1))