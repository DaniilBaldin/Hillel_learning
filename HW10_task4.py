new_dict = {1: 'entry 1', 2: 'entry 2', 3: 'entry 3', 4: 'entry 4'}
new_dict.pop(4)
new_list = []
for i in new_dict.items():
    new_list.append(tuple(i))
print(new_list)
