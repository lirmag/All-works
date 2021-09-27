list = []
def new_function(number):
    s = number
    n = 1
    while s < 60:
        s = s + 5
        n = n * 3
    return n
for i in range (1,61):
    if new_function(i) == 81:
        list.append(i)
print(list)