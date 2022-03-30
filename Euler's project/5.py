<<<<<<< HEAD
import math
# import datetime
#
# start = datetime.datetime.now()
#
#
# def compute():
#     answer = 1
#     print('i','answer','gcd')
#     for i in range(1, 11):
#
#         answer = (answer * i) // (math.gcd(i, answer))
#         print(i,answer,math.gcd(i,answer))
#     return answer
#
#
# if __name__ == "__main__":
#     print(compute())
#     print(datetime.datetime.now() - start)
print(math.gcd(1620,8))
=======
# def dig(number):
#     for i in range(1,21):
#         if (number % i) != 0:
#             return False
#     return True
#
#
# for number in range(2520,1000000001):
#     if dig(number):
#         print(number)
#         break


k = list(range(1,21,1))
for number in range(2520,1000000001):
    if all(number % dig == 0 for dig in k):
        print(number)
        break
>>>>>>> 3cfb42518cf1992d38b154c402330df81c069c44
