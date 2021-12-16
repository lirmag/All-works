length = int(input())
maximum = 0
s_maximum = 0
string = ''
for x in range(1,length + 1):
    num = input()
    if int(num) > maximum:
        s_maximum, maximum = maximum, int(num)
    elif int(num) > s_maximum:
        s_maximum = int(num)
print(s_maximum)
