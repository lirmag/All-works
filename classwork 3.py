even = 0
odd = 0
number = int(input())
number = str(number)
for i in range(0, len(number)):
    if int(number[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
even = str(even) + str(',') + str('|')
print('Even:', even, 'odd:', odd)
