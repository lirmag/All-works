import os
import random


def mk_txt(k):
    f = open(str(k) + 'txt', 'w+')
    f.close()


for k in range(1, 11):
    mk_txt(k)
f = open(str(random.randint(1, 10)) + 'txt', 'w+')
f.write('Hello')
f.close()


def del_txt(i):
    s = open(str(i) + 'txt', 'r')
    if 'Hello' not in s:
        s.close()
        os.remove(str(i) + 'txt')


for i in range(1, 11):
    del_txt(i)

# os.remove(str(3) + 'txt')
