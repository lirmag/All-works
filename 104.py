list = int(input())
row = []
row.append(list)
while list > 0:
    list -= 1
    row.append(list)
print(sum(row))