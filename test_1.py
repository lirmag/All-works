<<<<<<< HEAD
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
=======
n = 250
number = 3
c = (str(number)) * n
while '3333' in c or '7777' in c:
    if '3333' in c:
        c = c.replace('3333', '7', 1)
    else:
        c = c.replace('777', '3', 1)
print(c)
>>>>>>> 6069a0d60c9cf009b9365e4ee5c9e2fba3505570
