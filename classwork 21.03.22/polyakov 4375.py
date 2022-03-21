with open('4375.txt','r') as f:
    s = f.readline().strip()
s = s * 2
count = 1
ans = []
for index in range(0,len(s) - 1):
    if s[index] <= s[index + 1]:
        count += 1
    else:
        ans.append(count)
        count = 1
print(max(ans))