c = open('24_demo.txt','r')
lines = c.readlines()
k = []
count = 0
for line in lines:
    for el in line:
        k.append(el)


for index in range(0,len(k)):
    if k[index] == 'X' and k[index + 1] == 'Y' and k[index + 2] == 'Z':
        count += 1

print(count)