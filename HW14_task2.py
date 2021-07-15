list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Удаляем нечетные числа из первого и третьего списков
filtered_list_1 = list(filter(lambda x: x % 2 == 0, list_1))
filtered_list_3 = list(filter(lambda x: x % 2 == 0, list_3))
print(filtered_list_1)
print(filtered_list_3)

# Удаляем четные числа из второго списка
filtered_list_2 = list(filter(lambda x: not x % 2 == 0, list_2))
print(filtered_list_2)

# Объединяем списки в один список кортежей пар
zipped_list = list(zip(list_1, list_2, list_3))
print(zipped_list)

# Определяем сумму значений кортежей
sum_list = list(map(sum, zipped_list))
print(sum_list)

# Oставиv в sum_list только нечетные значения
final_list = list(filter(lambda x: not x % 2 == 0, sum_list))
print(final_list)