for number in range(123450708,123459799):
    number = str(number)
    if (number[6] == '7') and (number[8] == '8') and (int(number) % 23 == 0):
        print(number,int(number) // 23)