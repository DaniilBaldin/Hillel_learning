a_dictionary = {"a": 1, "b": 2, "c": 3}
new_list = []
for i in a_dictionary.items():
    new_list.append(tuple(i))
print(new_list)
