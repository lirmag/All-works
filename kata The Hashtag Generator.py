def generate_hashtag(s):
    if s == '' or s == ' ':
        return 0
    lst = s.split(' ')
    print(lst)
    ans = '#'
    for elem in lst:
        if elem == '':
            continue
        if lst == '.':
            continue
        a = elem[0]
        a = a.upper()
        for ind in range(1,len(elem)):
            b = elem[ind]
            if b == b.upper():
                elem = elem.replace(b,b.lower(),1)
        elem = a + elem[1:]
        ans += elem
    if (len(ans) > 140) or (ans == '') or (ans == ' '):
        return 0
    else:
        return ans
print(generate_hashtag('CodeWars is nice'))