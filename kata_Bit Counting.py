def count_bits(n):
    n = bin(n)[2:]
    count = 0
    for elem in n:
        if elem == '1':
            count += 1
    return count