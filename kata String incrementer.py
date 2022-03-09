def f(string):
    k = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number = ''
    for elem in range(0, len(string)):
        if string[elem] in k:
            count = elem
            a = string[0:elem]
            for el in range(elem, len(string)):
                while string[el] in k:
                    number += string[el]
                    break
    if len(number) != 0:
        string = a + str(int(number) + 1)
    else:
        string = string + '1'
    return string


print(f('foobar23'))
