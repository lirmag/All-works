def new_function(number):
    s = number
    n = 36
    while s < 2020:
        s = s * 2
        n = n + 3
    return (n)
for i in range(1, 5000):
    if new_function(i) == 60:
        print(i)