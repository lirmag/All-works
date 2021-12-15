date = input()
k = date.split()
count = 0
num = int(k[1])
while (num - 10) >= int(k[0]):
    count += 1
    num -= 10
print(count)