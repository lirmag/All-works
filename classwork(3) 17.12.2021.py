ans = ''
i = 1
while len(ans) < 32768:
    ans += ''.join(list(map(str, range(1, i))))
    i += 1
N = int(input())
print(ans[N - 1])
