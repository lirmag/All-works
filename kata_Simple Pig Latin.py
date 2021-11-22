def f(n):
    k = []
    n = n.split(' ')
    for elem in n:
        if elem == '.' or elem =='!' or elem == '?':
            k.append(elem)
        else:
            k.append(elem[1:len(elem)] + (elem[0] + 'ay'))
    a = ' '.join(k)
    return a
print(f('Pig latin is cool'))