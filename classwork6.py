import os
import random

for i in range(1, 11):
    f = open(str(i) + 'txt', 'w+')
f = open(str(random.randint(1, 10)) + 'txt','w+')
f.write('Hello')
f.close()
for i in range(1,11):
    s = open(str(i) + 'txt', 'r')
    s.readlines()
    if 'Hello' in s:
        continue
    else:
        os.remove(str(i) + 'txt')
    s.close()
# for i in range(1,11):
#     os.remove(str(i) + 'txt')
