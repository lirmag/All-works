number = 8**20 + ((8**22 - 8**17) * (8**13 + 8**16))
print(number)
ans = ''
while number > 0:
    ans = ans + str(number % 8)
    number //= 8

ans = ans[::-1]
print(ans)
while '7' in ans:
    ans = ans.replace('7','0',1)
print(ans)
ans = ans[3::]
ans = map(int,ans)
print(sum(ans))
