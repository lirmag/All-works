import random

seq = []
for i in range(1, 16):
    seq.append(random.randint(1, 100))
print(seq)


def sum_1(a):
    answer = 0
    for elem in a:
        answer += elem
    return answer


print(sum_1(seq))


def sum_2(a):
    answer = 0
    i = 0
    while i < (len(seq)):
        answer += seq[i]
        i += 1
    return answer


print(sum_2(seq))
