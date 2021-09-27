def my_function(list):
    answer = []
    for i in list:
        if i ** 0.5 * 10 % 10 == 0:
            answer.append(int(i**0.5))
        else:
            answer.append(i ** 2)
    return answer
print(my_function([4,3,9,7,2,1]))