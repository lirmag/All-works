import datetime
from datetime import datetime

lessons_start = {8: 45,
                 9: 35,
                 10: 35,
                 11: 25,
                 12: 15,
                 13: 15,
                 14: 5}
lessons_end = {9: 25,
               10: 15,
               11: 15,
               '12':'5',
               12: 55,
               13: 55,
               14: 45}
a = datetime.now()
now = a.replace(hour=9,minute=45,second=0,microsecond=0)
for el in lessons_start:
    flag = True
    for elem in lessons_end:
        les_s = now.replace(hour=el, minute=int(lessons_start.get(el)),second=0,microsecond=0)
        les_d = now.replace(hour=int(elem), minute=int(lessons_end.get(elem)),second=0,microsecond=0)
        if les_s < now and les_d > now:
            print('Урок уже идёт!')
            flag = False
        if les_d < now and les_s > now:
            print('До начала урока осталось:' + str(les_s - now)[2:4])
            flag = False
        else:
            break
        if flag == False:
            break
    if flag == False:
        break
# for el in now:
#     if el == ':':
#         now = now.replace(':','.')
#         now = float(now)
