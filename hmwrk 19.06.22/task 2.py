with open('17 (3).txt','r') as f:
    k = int(f.readline())
    a = [int(f.readline()) for i in range(k)]
    a.sort(reverse=True)
mx = a[0]
count = 1
for i in range(1,k):
    if a[i] <= mx - 5:
        count += 1
        mmx = a[i]
print(count,a[-1])