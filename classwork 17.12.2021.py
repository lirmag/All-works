length = int(input())
ans = 0
count = 1
while count != length:
    ans += count * (count + 1)
    print(count, '*', count + 1, '+', end=' ')
    if count == length - 1:
        print(count, '*', count + 1, '=', ans,end=' ')
    count += 1
