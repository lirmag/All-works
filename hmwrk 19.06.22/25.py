def f(number):
    k =[]
    i = 2
    while i ** 2 < number:
        if number % i == 0:
            k.append(i)
            k.append(number // i)
        i += 1
        if i ** 2 == number:
            k.append(i)
    return len(k)

list = list(range(245690,245757))


for count,number in enumerate(list,start=1):
    if f(number) == 0:
        print(count,number)