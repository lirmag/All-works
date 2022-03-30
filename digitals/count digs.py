import datetime

start = datetime.datetime.now()


def dig(number):
    count = 2
    i = 2
    while i ** 2 < number:
        if number % i == 0:
            count += 2
        i += 1
        if number ** 2 == number:
            count += 1
    return count


print(dig(10**8))
print(datetime.datetime.now() - start)
