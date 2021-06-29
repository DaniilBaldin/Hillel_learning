list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_x = [(x, y) for x, y in zip(list_a, list_a)]
list_c = [(list_a[i],list_b[i]) for i in range(len(list_a))]
print(list_c)
