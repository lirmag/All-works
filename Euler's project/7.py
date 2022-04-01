import tqdm
from tqdm import trange
from time import sleep


count = 0
for number in trange(5001,desc='Bar',ncols=200,colour='MAGENTA',nrows=1000):
    if count == 10001:
        print(number)
        break
    if all(number % dig != 0 for dig in range(2, round(number // 2) + 1)):
        count += 1
    sleep(.1)
