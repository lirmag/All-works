answer = []
for i in range(2,1001,2):
    for j in range(1,1002,2):
        number = (2**i) * (3**j)
        if 400000000 < number < 600000000:
            answer.append(number)
print(answer)