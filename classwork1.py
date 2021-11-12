n = int(input())
n = str(n)
if n[len(n) - 1] == '1':
    print(n, 'Корова')
if n[len(n) - 1] == '0' or n[len(n) - 1] =='5' or n[len(n) - 1] == '6' or n[len(n) - 1] == '7' or n[len(n) - 1]== '8' or n[len(n) - 1] == '9':
    print(n, 'Коров')
if n[len(n) - 1] == '2' or n[len(n) - 1] == '3' or n[len(n) - 1] == '4':
    print(n, 'Коровы')
