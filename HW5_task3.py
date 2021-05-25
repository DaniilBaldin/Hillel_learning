from math import sqrt

x = float(input("x="))
y = float(input("y="))
r = float(input("r="))
h = sqrt(x ** 2 + y ** 2)
print("Расстояние до точки от начала координат равно %.2f" % h)
if h > r:
    print("точка находится за пределами круга")
else:
    print("точка принадлежит кругу")