def find_outlier(integers):
    count = 0
    for el in integers:
        if el % 2 == 0:
            count += 1
            if count == 2:
                count = 0
                for elem in integers:
                    if elem % 2 != 0:
                        return elem
    for el in integers:
        if el % 2 != 0:
            count += 1
            if count == 2:
                for elem in integers:
                    if elem % 2 == 0:
                        return elem
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

