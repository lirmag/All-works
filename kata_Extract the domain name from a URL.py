def domain_name(url):
    ans = ''
    for el in url[7:]:
        if el != '.':
            ans += el
        if el == '.' or el == '/' or el == ':' or el == 's':
            continue
    # while 'w' in ans or 'com' in ans or '.' in ans:
    #     if 'w' in ans:
    #         ans = ans.replace('w','',1)
    #     if '.' in ans:
    #         ans = ans.replace('.','',1)
    #     if 'com' in ans:
    #         ans = ans.replace('com','',1)
    return ans
print(domain_name("www.xakep.ru"))