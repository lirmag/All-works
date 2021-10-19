workers = [
    {"name": "Александр", "lastname": "Леонов", "age": 35, "role": "Менеджер по продажам",
     "achievements": ["Менеджер месяца (Март 2019)", "Лучшая промо активность (Апрель 2019)"]},
    {"name": "Иван", "lastname": "Петров", "age": 56, "role": "Охранник", "achievements": []},
    {"name": "Олег", "lastname": "Бубликов", "age": 32, "role": "Менеджер по продажам",
     "achievements": ["Менеджер месяца (Июнь 2019)", "Менеджер месяца (Июль 2019)",
                      "Лучший старт продаж нового бренда (Август 2019)"]},
    {"name": "Анна", "lastname": "Ветрова", "age": 27, "role": "Бухгалтер", "achievements": []},
    {"name": "Геннадий", "lastname": "Сталеваров", "age": 45, "role": "Директор",
     "achievements": ["Лучшее предприятие года (2017)", "Лучшее предприятие года (2018)",
                      "Лучшие показатели по дистрибьюции нового продукта XYZ (Март 2019)"]}
]
average_age = 0
number_workers = 0
a = len(workers) - 1
b = 0

m = 0
n = 0
k = 0
while a != -1:
    average_age += workers[a].get('age')
    number_workers += 1
    a -= 1
print('Средний возраст сотрудников:', int(average_age / number_workers))
while b != (len(workers)):
    print(workers[b].get('lastname'), workers[b].get('name'), ('(' + (workers[b].get('role')) + ')'))
    print('Достижения:')
    if len(workers[b].get('achievements')) > 0:
        print(' ', (str(workers[b].get('achievements'))) + '\n')
    for i in (workers[b].get('achievements')):
        for j in len(workers[b].get('achievements')):
            print(' ', (str(workers[b].get('achievements')[j])) + '\n')
            j -= 1
        # print(' ', str(workers[b].get('achievements')[2]) + '\n')
        # j += 1
        # for i in range(j):
        #     print(' ', str(workers[b].get('achievements')) + '\n')
    else:
        print(' ', 'Достижений нет!' + '\n')
    b += 1

