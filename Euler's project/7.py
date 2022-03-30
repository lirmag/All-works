count = 0
for number in range(2,1000000001):
    if count == 10001:
        print(number)
        break
    if all(number % dig != 0 for dig in range(2,round(number // 2) + 1)):
        count += 1