<<<<<<< HEAD
string = '[b]fsdfds'
print('[b]' in string)
=======
def between_markers(text: str, begin: str, end: str) -> str:
    for ind in range(0,len(text)):
        if text[ind] == begin[-1]:
            start = ind + 1
        if text[ind] == end[0]:
            finish = ind
    if (begin in text) and (end in text):
        return text[start:finish]
    if (begin not in text) and (end in text):
        return text[0:finish]
    if (begin in text) and (end not in text):
        return text[start::]
    if (begin not in text) and (end not in text):
        return text


# print(between_markers('What is >apple<', '>', '<'))
print(between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>"))
>>>>>>> 9c1552ac13d854bb8a23f40b3baeb0b745816f9a
