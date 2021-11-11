f = open('inf_26_04_21_26 (1).txt','r')
lines = f.readlines()
k = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
print(k)