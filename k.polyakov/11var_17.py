c = open('05', 'r')
lines = c.readlines()
k = []
count = 0
sum_1 = []
for elem in lines:
    elem = int(elem)
    k.append(elem)
for index in range(0, len(k) - 2):
    if ((bin(k[index])[2:].count('1') == 2) and (bin(k[index + 1])[2:].count('1') == 2) and (
            bin(k[index])[2:].count('0') >= 1) and (bin(k[index + 1])[2:].count('0') >= 1)) or (
            (bin(k[index])[2:].count('1') == 2) and (bin(k[index + 2])[2:].count('1') == 2) and (
            bin(k[index])[2:].count('0') >= 1) and (bin(k[index + 2])[2:].count('0') >= 1)) or (
            (bin(k[index + 1])[2:].count('1') == 2) and (bin(k[index + 2])[2:].count('1') == 2) and (
            bin(k[index + 1])[2:].count('0') >= 1) and (bin(k[index + 2])[2:].count('0') >= 1)):
        count += 1
        sum_1.append(max(k[index], k[index + 1], k[index + 2]))
print(count, sum(sum_1))
