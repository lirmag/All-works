def create_phone_number(n):
    step_1 = ''
    step_2 = ''
    step_3 = ''
    ans = ''
    for el in range(0,3):
        step_1 += str(n[el])
        if el == 2:
            step_1 = '(' + step_1 + ') '
    for el in range(3,6):
        step_2+= str(n[el])
        if el == 5:
            step_2 = step_2 + '-'
    for el in range(6,10):
        step_3 += str(n[el])
    ans = step_1 + step_2 + step_3
    return ans
print(create_phone_number(([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])))