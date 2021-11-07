# k = (True,False)
# print('x y z w f')
# for x in k:
#     for y in k:
#         for z in k:
#             for w in k:
#                 f = (x == (not y)) >= (z == (y or w))
#                 if f is False:
#                     print(int(x), int(y), int(z), int(w), int(f))

# for number in range(1,101):
#     answer = number
#     answer = (bin(answer)[2:].zfill(8))
#     if '1' in answer:
#         answer = answer.replace('1', 'U')
#     if '0' in answer:
#         answer = answer.replace('0', '1')
#     if 'U' in answer:
#         answer = answer.replace('U', '0')
#     answer = int(answer, base=2)
#     if answer - number == 133:
#         print(number)

def f(number):
    s = number
    n = 1
    while s > 0:
        s = s - 9
        n = n + 4
    return n
print(f(47))

# 7
Способ
# А.Общее
# время
# складывается
# из
# времени
# сжатия, распаковки
# и
# передачи.Время
# передачи
# t
# рассчитывается
# по
# формуле
# t = Q / q, где
# Q — объём
# информации, q — cкорость
# передачи
# данных.
#
# Найдём
# сжатый
# объём: 10 * 0, 3 = 3
# Мбайта
#
# Переведём
# Q
# из
# Мбайт
# в
# биты: 3
# Мбайта = 3 * 220
# байт = 3 * 223
# бит.
#
# Найдём
# общее
# время: t = 7
# с + 1
# с + 3 * 223
# бит / 218
# бит / с = 8 + 3 * 25
# с = 104
# с.
#
# Способ
# Б.Общее
# время
# совпадает
# с
# временем
# передачи: t = 10 * 223
# бит / 218
# бит / с = 10 * 25
# с = 320
# с.
#
# Видно, что
# способ
# A
# быстрее
# на
# 320 - 104 = 216
# с.
#
# Ответ: A216.