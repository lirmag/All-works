with open('107_24.txt','r') as f:
    s = f.read()
s = s.replace('CB','x')
s = s.replace('AB','x')
count = 0
sm = []
for ind in range(0,len(s) - 1):
    if s[ind] == 'x':
        count += 1
    else:
        sm.append(count)
        count = 0
print(max(sm))




