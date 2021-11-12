import os
import random

for i in range(1, 11):
    f = open(str(i) + 'txt', 'w+')
    f.close()
f = open(str(random.randint(1, 10)) + 'txt', 'w+')
f.write('Hello')
f.close()
for i in range(1, 11):
    s = open(str(i) + 'txt', 'r')
    if 'Hello' in s:
        continue
    s.close()
    os.remove(str(i) + 'txt')

# os.remove(str(3) + 'txt')
