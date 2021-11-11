number = ((4 ** 14) + (2 ** 32) -4)
number = bin(number)[2:]
count = 0
for i in range(0,len(number) - 1):
    if number[i] == '1':
        count += 1
print(count)