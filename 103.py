def my_function(row):
    b = 0
    sum = 0
    while row - 1 > b:
        b = b + 1
        print(b, '+' , end="")
        sum += b
my_function (int(input()))
