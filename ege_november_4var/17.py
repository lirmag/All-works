f = open('17 (4).txt','r')
lines = f.readlines()
k = []
raz = []
for element in lines:
    element = int(element)
    k.append(element)
s = 0
count = 0
for i in range(0,len(k) - 1):
    s += 1
    for j in range(s,len(k)):
        if ((k[i] - k[j]) % 60 == 0) and ((k[i] % 15 == 0) or (k[j] % 15 == 0)):
            count += 1
            raz.append(k[i] - k[j])
print(count)
print(max(raz))
