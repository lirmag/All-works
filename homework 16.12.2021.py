length = int(input())
mix = 0
s_mix = 0
string = ''
for x in range(1,length + 1):
    num = input()
    if int(num) > mix:
        s_mix, mix = mix, int(num)
    elif int(num) > s_mix:
        s_mix = int(num)
print(s_mix)
