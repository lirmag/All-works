# 8358 2324
with open('27880.txt', 'r') as f:
    s = sorted(list(map(int, f.readlines())))


ctg = []
a = []
i = 0
sm = 0
count = 0

for b in range(0,len(s) - 1):
    for index in range(b,len(s) - 1):
        if s[index] + sm < 8358:
            count += 1
            sm += s[index]
            ctg.append(s[index])
        else:
            a.append(count)
            sm = 0
            count = 0
            break
print(max(a),max(ctg))
