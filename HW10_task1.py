list_1 = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]
tuple_1 = tuple(list_1)
print(tuple_1)
list_2 = [(d['color'], d['value']) for d in tuple_1]
print(list_2)
