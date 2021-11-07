f = open('17 (1).txt')
a = f.readlines()
a = list(map(int,a))
count = 0
m = 19999
delete = 0
k = []
for number in a:
    a.remove(number)
    for number_1 in a:
        # if number == number_1:
        #     continue
        if (int(number) * int(number_1)) % 10 == 0:
            count += 1
            m = max(m, int(number) + int(number_1))
print(count)
print(m)