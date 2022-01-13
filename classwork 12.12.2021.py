N = input()
maximum = 0
minimum = int(N[0])
for number in N:
    if int(number) > maximum:
        maximum = int(number)
    if int(number) < minimum:
        minimum = int(number)
print(maximum)
print(minimum)
