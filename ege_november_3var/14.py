a = 12
b = 13
c = 211
for base in range(5,7):
    answer = ''
    answer_1 = ''
    answer_2 = ''
    while a > 0:
        answer = answer + str(a % base)
        a //= base
    while b > 0:
        answer_1 = answer_1 + str(b % base)
        b //= base
    while c > 0:
        answer_2 = answer_2 + str(c % base)
        c //= base
    if (int(answer) * int(answer_1)) == int(answer_2):
        print(base)
    else:
        answer = ''
        answer_1 = ''
        answer_2 = ''
        a = 12
        b = 13
        c = 211
        continue