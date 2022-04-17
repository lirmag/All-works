def frequency_sort(items):
    d = dict()
    s_d = dict()
    l = []
    a = []
    for elem in items:
        d[elem] = items.count(elem)
    items.clear()
    # l = sorted(d,key=d.get)
    for el in d:
        l.append(d.get(el))
    for elem in l:
        for el in d:
            if elem > d.get(elem):
                flag = True
            else:
                flag = False
        if flag == True:
            a.append(elem)
    for w in l:
        s_d[w] = d[w]
    for elem in l:
        for count in range(0,d.get(elem)):
            items.append(elem)
    return items


# print((frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))
# print(frequency_sort([4,6,2,2,2,6,4,4,4]))
print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])))