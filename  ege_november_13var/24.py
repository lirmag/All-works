f = open('inf_26_04_21_24.txt','r')
lines = f.readlines()
x = 1
answer = []
for line in lines:
    if line.count('A') <= 25:
        print(line.count('A'))
        for elem in line:
            count = 0
            for el in range(line[x + 1],elem,-1):
                if elem == el:
                    answer.append(count)
                    count = 0
                    x += 1
                    break
                else:
                    count += 1
                    continue

print(max(answer))
