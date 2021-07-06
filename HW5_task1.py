from random import random
a = int(random() * 1000)
b = int(random() * 1000)
print(a, b)
if a % 2 == 1:
    print('Число a нечетное:', a)
if b % 2 == 1:
    print('Число b нечетное:', b)
