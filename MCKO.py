# zadanie 1:
k = (True,False)
print('x y z w f')
for x in k:
    for y in k:
        for z in k:
            for w in k:
                f = not (x and y) and ( y or z) or not w
                if f is False:
                    print(int(x), int(y), int(z), int(w), int(f))
# Otvet: ywzx

# Zadanie 2:
k = []
for i in range(1, 100001):
    digit = i
    two_count = ''
    sum_1 = 0
    c = two_count
    while digit > 0:
        two_count = str(digit % 2) + two_count  # Перевод в двоичную систему счисления
        digit //= 2


    def suma(c):
        sum_1 = 0
        while int(c) > 0:
            count = int(c) % 10
            sum_1 += int(count) # Функция вычисления суммы чисел в числе
            c = int(c) // 10
        return sum_1


    digit_two = (str(two_count) + str(sum_1 % 2))
    answer = (str(digit_two) + str(suma(int(digit_two)) % 2))
    answer = int(answer, base=2)
    if int(answer) < 98:
        k.append(i)
print(max(k))
# Otvet: 24

# Zadanie 3:
k = []


def f(number):
    s = number
    n = 1
    n = 1
    while s < 45:
        s = s + 6
        n = n * 4
    return n


for number in range(1, 1001):
    if f(number) == 256:
        k.append(number)
print(max(k))
# Otvet: 26

# Zadanie 4:
# Sdelat' ruschkami
# Otvet: 256

# Zadanie 5:
# Sdelat' ruschkami
# Otvet: 270

# Zadanie 6:
# excel

# Zadanie 7:
# Otvet: 8

# Zadanie 8:
# Hz

# Zadanie 9:
n = 250
number = 3
c = (str(number)) * n
print(c)
while ('3333' in c) or ('7777' in c):
    if '3333' in c:
        c = c.replace('3333', '3333,7')
    else:
        c = c.replace('7777', '777,3')
print(c)

# Zadanie 10:
c = int(64 ** 9) + int(8 ** 25) - int(9)
newNum = ''
while c > 0:
    newNum = str(c % 8) + newNum
    c //= 8
print(newNum)
Otvet: 17

# Zadanie 11:
def f(A, x):
    if A % x == 0:
        return 1
    else:
        return 0
A = 1
while True:
    for x in range(1,1000000):
        if  (not f(A, 34)) and (f(283, x) <= (not f(A, x) <= (not f(120, x)))):
            break
        else:
            print(A)
    A += 1
Otvet: 34

# Zadanie 12:
# hz

# Zadanie 13:
k = []
def f(n):
    x = n
    L = 0
    M = 0
    while x > 0:
        M = M + 2
        if x % 8 != 0:
            L = L + 1
        x = x // 8
    return L, M
for n in range(1,10000):
    if f(n) == (2,6):
        k.append(n)
print(min(k))
Otvet: 65