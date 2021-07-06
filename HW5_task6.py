a = int(input("Длина стороны a = "))
b = int(input("Длина стороны b = "))
c = int(input("Длина стороны c = "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")
