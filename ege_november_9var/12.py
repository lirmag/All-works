string = str(1) + (str(9) * 98)
while ('19' in string) or ('299' in string) or ('3999' in string):
    string = string.replace('19', '2', 1)
    string = string.replace('299', '3', 1)
    string = string.replace('3999', '1', 1)
print(string)