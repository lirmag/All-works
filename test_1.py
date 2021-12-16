<<<<<<< HEAD
print(12 & 34)
=======
def to_underscore(string):
    if type(string) == int:
        return str(string)
    ans = ''
    a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    string = string[0].lower() + string[1:]
    for el in string:
        if el not in a:
            ans += el
        if el in a:
            ans += '_' + el.lower()
    return ans
>>>>>>> 711acdbd897995d19b49f52f2a9a2002260b5447
