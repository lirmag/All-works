with open('27886 (1).txt','r') as f:
    data = f.readlines()
S,_ = map(int,data[0].split())
del data[0]
data = sorted(list(map(int,data)))
total = 0
for n,var in enumerate(data):
    if total + var > S:
        break
    total += var
print(n)
d = S - total
cand = [x for x in data if x - data[n - 1] <= d]
print(max(cand))