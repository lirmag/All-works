sub = int(input())
sum = 0
for i in range(sub):
    num = int(input())
    if num % 10 == 9:
        sum += 1
print(sum)