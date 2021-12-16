f = open('24 (2).txt','r')
s = f.read().split('A')
m = 0
for ind in range(0,len(s) - 1):
    if len(s[ind]) + len(s[ind + 1]) + 1 > m:
        m = len(s[ind]) + len(s[ind + 1]) + 1
print(m)
