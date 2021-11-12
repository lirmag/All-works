import random

seq = []
answer = []
for i in range(1, 11):
    seq.append(random.randint(1, 100))
print(seq)
for ind in range(0, len(seq) - 1):
    if (seq[ind] > 35) and (seq[ind] < 65):
        answer.append(seq[ind])
for el in answer:
    for elem in seq:
        if el == elem:
            seq.remove(el)
print(seq)
print(answer)
