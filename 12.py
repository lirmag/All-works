sequence = []
sequence_2 = []
print('Напишите количество чисел в последовательности:')
elements = int(input())
print('Напишите числа в последовательности:')
for i in range(elements):
    new = int(input())
    sequence.append(new)
print(sequence)
for i in sequence:
    if i > 0:
        sequence_2.append(i)
print(min(sequence_2))