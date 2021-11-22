def find_it(seq):
    for elem in seq:
        if seq.count(elem) % 2 != 0:
            return elem
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))