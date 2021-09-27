<<<<<<< HEAD
sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for u in sequence:
    if u < 5:
        b.append(u)
print(b)

=======
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
>>>>>>> c669bbec56fe9b2689ad1f8164d825f86c068711
