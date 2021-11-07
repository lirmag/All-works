number = 9575
k = []
number = str(number)
k.append((int(number[0]) + int(number[1])))
k.append((int(number[1]) + int(number[2])))
k.append((int(number[2]) + int(number[3])))
k.remove(min(k))
answer = str(min(k)) + str(max(k))
print(k)
print(answer)