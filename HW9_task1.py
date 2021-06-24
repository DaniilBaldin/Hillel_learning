dct = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print(id(dct))

# Меняем местами первый и последний элементы
dct_2 = dct.copy()
my_list = list(dct_2.items())
print(my_list)
first_el = my_list[0]
last_el = my_list[-1]
key_first_el = first_el[0]
key_last_el = last_el[0]
value_first_el = first_el[1]
value_last_el = last_el[1]
my_list.pop(0)
my_list.pop(-1)
my_list.insert(0, last_el)
my_list.insert(4, first_el)
print(my_list)
dct_2 = dict(my_list)
print(dct_2)

# Удаляем второй элемент
second = list(dct.items())[1]
del dct[second[0]]
print(dct)

# Вставляем новый элемент
dct['new_key'] = 'new_value'
print(dct)
print(id(dct))
print(id(dct))
