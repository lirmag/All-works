def zeros(n):
    if n == 0 or n == 1:
        return 0
    ans = 1
    while n != 1:
        ans *= n
        n -= 1
    ans = str(ans)[::-1]
    count = 0
    for el in ans:
        if el == '0':
            count += 1
        if el != '0':
            break
    return count
print(zeros(30))