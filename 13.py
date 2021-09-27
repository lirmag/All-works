def new_function(number):
    s = number
    n = 1024
    while s >= 5:
        s = s - 5
        n = n // 2
    return n
for i in range (1,2000):
    if new_function(i) == 64:
        print(i)