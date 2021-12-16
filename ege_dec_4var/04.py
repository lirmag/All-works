num = '101011100001010'
num = int(num,base=2)
ans = ''
while num > 0:
    ans = ans + str(num % 8)
    num //= 8
print(ans[::-1])