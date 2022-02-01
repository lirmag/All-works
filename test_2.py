import datetime
from datetime import datetime


now = datetime.now()
hrs = int(now[11:13])
mnt = int(now[14:16])
mnt += hrs * 60
# mnt = 900
# maximum = 886
# func = 'working'
def counting_time(mnt):
    maximum = 936
    func = 'working'
    lessons_start = {525: 565,
                     575: 615,
                     635: 675,
                     685: 725,
                     735: 775,
                     795: 835,
                     845: 885,
                     895: 935}
    for elem in lessons_start:
        if elem < mnt and lessons_start[elem] > mnt:
            func = 'done'
            return str('The lesson is already in progress!')
    if func == 'working':
        for elem in lessons_start:
            if mnt - lessons_start[elem] > 0:
                for el in lessons_start:
                    if mnt > maximum:
                        return str('Lessons are already over!')
                    if mnt < el:
                        if el - mnt == 1:
                            min = ' minute'
                        else:
                            min = ' minutes'
                        ans = str(el - mnt) + min + ' to go before the lesson starts!'
                        return ans


print(counting_time(886))
# lessons_end = {9: 25,
#                10: 15,
#                11: 15,
#                '12':'5',
#                12: 55,
#                13: 55,
#                14: 45}
