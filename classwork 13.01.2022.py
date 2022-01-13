def human_readable(number):
    hundreds_units = {'0': '',
                      '1': 'one',
                      '2': 'two',
                      '3': 'three',
                      '4': 'four',
                      '5': 'five',
                      '6': 'six',
                      '7': 'seven',
                      '8': 'eight',
                      '9': 'nine'}
    dozens = {'0': '',
              '2': 'twenty',
              '3': 'thirty',
              '4': 'forty',
              '5': 'fifty',
              '6': 'sixty',
              '7': 'seventy',
              '8': 'eighty',
              '9': 'ninety'}
    exceptions = {'10': 'ten',
                  '11': 'eleven',
                  '12': 'twelve',
                  '13': 'thirteen',
                  '14': 'fourteen',
                  '15': 'fifteen',
                  '16': 'sixteen',
                  '17': 'seventeen',
                  '18': 'eighteen',
                  '19': 'nineteen'}
    ans = ''
    if len(number) == 3:
        if int(number[0]) > 1:
            hun = 'hundreds'
        else:
            hun = 'hundred'
        ans = ans + hundreds_units[number[0]] + ' ' + hun
        if number[1] == '0':
            ans = ans + dozens[number[1]] + ' '
            ans = ans + hundreds_units[number[2]]
            return ans
        if number[1] != '1' and number[1] != '0':
            ans = ans + ' ' + dozens[number[1]] + ' '
            ans = ans + hundreds_units[number[2]] + ' '
            return ans
        if number[1] == '1' and number[1] != '0':
            ans = ans + ' ' + exceptions[number[1] + number[2]]
            return ans
    if len(number) == 2:
        if number[0] != '1':
            ans = ans + dozens[number[0]] + ' '
            ans = ans + hundreds_units[number[1]]
            return ans
        else:
            ans = ans + exceptions[number]
            return ans
    if len(number) == 1:
        ans = ans + hundreds_units[number]
        return ans


for number in range(1, 1000):
    print(str(number) + ' - ' + human_readable(str(number)))
