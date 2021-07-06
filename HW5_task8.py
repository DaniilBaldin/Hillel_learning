a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a % b == 0:
    print("%d делится на %d" % (a, b))
else:
    print("%d не делится на %d" % (a, b))
    print("Остаток: %d" % (a % b))
print("Частное: %d" % (a//b))
