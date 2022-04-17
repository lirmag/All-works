def counting(number):
    num = bin(number)[2:]
    if len(num) < 8:
        num = num.rjust(8,'0')
    num = num.replace('0','a')
    num = num.replace('1','b')
    num = num.replace('a','1')
    num = num.replace('b','0')
    return int(num,base=2)


for n in range(1,256):
    if counting(n) - n == 111:
        print(n)
        break