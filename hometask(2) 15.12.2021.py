date = input()
k = date.split()
us = 0
flag = True
if int(k[0]) > int(k[1]):
    flag = False
if (2000 >= int(k[1]) > 1605) and (flag is True) and (int(k[0]) <= 2000):
    # dig = int(k[1]) - int(k[0])
    # ans = dig // 10
    # print(ans)
    us = 1605 - int(k[0])
    if us <= 0:
        dig = int(k[1]) - int(k[0])
        ans = dig // 10
        print(ans)
    else:
        dig = int(k[1]) - int(k[0]) - us
        ans = dig // 10
        print(ans)
else:
    print(0)
