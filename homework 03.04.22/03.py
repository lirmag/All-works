number = 6 ** 1333 - 5 * 6 ** 1215 + 3 * 6 ** 144 - 86
ans = ''
while number > 0:
    ans = ans + str(number % 6)
    number //= 6
ans = str(sum(map(int, ans)))
# ans = str(sum(ans))
print(int(ans, base=6))
