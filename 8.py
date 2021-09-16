num = int(input())
sum = 0
pos = 0
neg = 0
while num != 0:
    sum += num
    if num > 0:
        pos += 1
    else:
        neg += 1
    num = int(input())
print(sum)
print(pos - neg)