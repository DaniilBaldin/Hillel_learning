a = int(input('Введите значение А:'))
b = int(input('Введите значение В:'))
c = int(input('Введите значение С:'))

d = a
if d < b:
    d = b
elif d < c:
    d = c

print('Наибольшее число: ', d)

