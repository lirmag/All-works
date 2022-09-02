# print(int('1', base=10))
# print(int('101', base=7))
for dig in range(2, 101):
    try:
        if int('121', base=dig) == 49:
            n = dig
            ans = ''
            while dig > 0:
                ans += str(dig % 3)
                dig //= 3
                print(ans[::-1])
    except:
        continue
