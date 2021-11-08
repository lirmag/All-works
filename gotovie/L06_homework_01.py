  # -*- coding: utf-8 -*-
"""
1) Напишите функцию common_elements(), которая принимает 2 аргумента (два разных списка)
2) Функция common_elements() должна возаращать новый список, который содержит в себе общие элементы. Например, даны 2 списка
    list_1 = ['python', 'windows', 'linux', 'macOS']
    list_2 = ['python', 'JavaScript', 'HTML', 'linux']
    
    result_list = ['python', 'linux']

3) выведите на экран результат работы программы используя переменную result_common и функцию common_elements(). В качестве аргументов используйте списки cars_1, cars_2

            Резульат работы программы:
                
                ['bmw', 'lexus']
                --------------------------------------------------
"""
result_common = []


def common_elements(cars_1, cars_2):
    for i in range(len(cars_1) - 1):
        for j in range(len(cars_2) - 1):
            if cars_1[i] == cars_2[j]:
                result_common.append(cars_1[i])
    return result_common


print(common_elements(['bmw', 'mercedes', 'lexus', 'mazda'], ['lexus', 'opel', 'bmw', 'kia', 'volvo']))
# Ваш код ниже
