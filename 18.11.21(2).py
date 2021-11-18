k = list(map(int, input().split()))
ans = []
for el in range(len(k) - 1, -1, -1):
    ans.append(k[el])
print(*ans)
