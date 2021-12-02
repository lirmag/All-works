def IsPrime(n):
    count = 0
    if n > 1:
        for dig in range(2, n // 2):
            if (dig != n) and (n % dig == 0):
                count += 1
                return 'False'
        if count == 0:
            return 'True'
    else:
        return 'False'


print(IsPrime(1))
