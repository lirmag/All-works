for number in range(1,256):
    n = bin(number)[2:].rjust(8,'0')
    n = n.replace('0','a')
    n = n.replace('1','b')
    n = n.replace('a','1')
    n = n.replace('b','0')
    n = int(n,base=2)
    if number - n == 133:
        print(number)
        break