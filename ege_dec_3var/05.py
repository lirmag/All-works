for number in range(0,256):
    a = number
    a = bin(a)[2:].zfill(8)
    a = a.replace('0','a')
    a = a.replace('1','b')
    a = a.replace('a','1')
    a = a.replace('b','0')
    a = int(a,base=2)
    ans = a - number
    if ans == 111:
        print(number)
        break