import telebot
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
=======
sum = 0
num = int(input())
while num != 0:
    if (num % 4 == 0) and (num % 10 == 2):
        sum += 1
    num = int(input())
print(sum)
>>>>>>> c669bbec56fe9b2689ad1f8164d825f86c068711
