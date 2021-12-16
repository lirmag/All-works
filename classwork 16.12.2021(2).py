string = input()
k = string.split(' ')
sum = 0
for elem in k:
    elem = int(elem)
    sum += elem
print(sum)