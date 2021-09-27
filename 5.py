sequence = []
print('Напишите количество чисел в последовательности')
elements = int(input())
print('Напишите числа в последовательности')
for i in range(elements):
    new = int(input())
    sequence.append(new)
print(list)
min = 0
for i in sequence:
    if i < min:
        min = i
print(min)
