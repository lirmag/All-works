sum = 0
num = int(input())
while num != 0:
    if (num % 4 == 0) and (num % 10 == 2):
        sum += 1
    num = int(input())
print(sum)