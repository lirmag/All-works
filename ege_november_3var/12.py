number = '>' + (str(1) * 10) + (str(2) * 20) + (str(3) * 30)
print(number)
while ('>1' in number) or ('>2' in number) or ('>3' in number):
    if '>1' in number:
        number = number.replace('>1','22>',1)
    if '>2' in number:
        number = number.replace('>2','2>',1)
    if '>3' in number:
        number = number.replace('>3', '1>',1)
print(number)
number = str(2222222222222222222222222222222222222222111111111111111111111111111111)
sum_1 = 0
for element in number:
    element = int(element)
    sum_1 += element
print(sum_1)