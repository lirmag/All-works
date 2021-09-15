num = 1
sum = 0
pos = 0
neg = 0
while num != 0:
    num = int(input())
    sum += num
    if num > 0:
        pos += 1
    else:
        neg += 1
print(sum)
print(pos - neg)


