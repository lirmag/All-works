# number = '6677'
# ans = ''
# s_number = number[::-1]
# t_number = str(int(number) + int(s_number))
# k = []
# for el in t_number:
#     el = int(el)
#     k.append(el)
# k = sorted(k)
# for el in k:
#     el = str(el)
#     ans += el
# print(ans)


def RATS(number,count):
    print(number)
    number = str(number)
    ans = ''
    k = 0
    while k != count:
        s = []
        k += 1
        s_number = number[::-1]
        t_number = str(int(number) + int(s_number))
        for el in t_number:
            el = int(el)
            s.append(el)
        for elem in sorted(s):
            elem = str(elem)
            ans += elem
        while ans[0] == '0':
            ans = ans[1:]
        number = ans
        print(ans)
        ans = ''
RATS(2022,40)