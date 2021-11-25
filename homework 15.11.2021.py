number = (3 * (216 **4)) + (2 * (36 ** 6)) - 648
ans = ''
while number > 0:
    ans = ans + str(number % 6)
    number //= 6
print(ans)
print(ans.count('5'))