test_list = [1, 1, 2, 3, 4, 4, 5]
non_unique = [i for i in set(test_list) if test_list.count(i) > 1]
if len(non_unique) == 0:
    print("Повторяющихся элементов нет")
else:
    print(non_unique)
