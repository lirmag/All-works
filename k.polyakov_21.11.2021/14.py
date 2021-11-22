number = str((64**25 + 4**10) - (16**20 + 32**3))
number = number[::-1]
print(number)
count = 0
for el in number:
    if el == '2':
        print(count)
        break
    else:
        count += 1
