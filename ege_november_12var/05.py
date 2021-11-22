count = 0
for num in range(100,1000):
    number = str(num)
    ans_1 = int(number[0]) + int(number[1])
    ans_2 = int(number[1]) + int(number[2])
    answer = str(max(ans_1,ans_2)) + str(min(ans_1,ans_2))
    if answer == '1715':
        count += 1
print(count)