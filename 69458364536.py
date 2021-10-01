# number = int(input())
list_1 = []
list_2 = []


def function_1(number):
    while number != 0:
        list_1.append(number)
        number = int(input())
    print(list_1)
    print(max(list_1))
    print(min(list_1))
    print(len(set(list_1)))
    if (sum(list_1)) % 5 == 0:
        print(list_2)
    for i in range(len(list_1)):
        if list_1[i] % 2 == 0:
            list_1[i] = -list_1[i]
    print(list_1)


function_1(1)
