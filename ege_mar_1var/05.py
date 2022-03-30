def f(number):
    s_1 = int(number[0]) + int(number[2]) + int(number[4])
    s_2 = int(number[1]) + int(number[3])
    return str(min(s_1,s_2)) + str(max(s_1,s_2))


for x in range(10000,99998):
    if f(str(x)) == '723':
        print(x)
        break

