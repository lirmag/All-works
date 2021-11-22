f = open('inf_26_04_21_24 (1).txt','r')
lines = f.readlines()
x = 1
answer = []
for line in lines:
    if line.count('G') <= 25:
        for el in line:
            count = 0
            for elem in range(line[x + 1],elem,- 1):
                if el == elem:
                    answer.append(count)
                    count = 0
                    x += 1
                    break
                else:
                    count += 1
                    continue
print(max(answer))