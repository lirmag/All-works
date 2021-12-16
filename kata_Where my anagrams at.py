def anagrams(word, words):
    ans = []
    for elem in words:
        flag = True
        for el in word:
            if (elem.count(el) == word.count(el)) and (len(word) == len(elem)):
                continue
            else:
                flag = False
        if flag == True:
            ans.append(elem)
    return ans
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
