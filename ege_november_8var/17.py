k = []
with open('17 (9).txt','r') as f:
    lines = f.readlines()
    for element in lines:
        k.append(int(element))
s = 0
count = 0
sum_1 = []
for i in range(0,len(k) - 1):
    s += 1
    for j in range(s,len(k)):
        if (k[i] - k[j]) % 80 == 0:
            count += 1
            sum_1.append(k[i] - k[j])
print(count,max(sum_1))