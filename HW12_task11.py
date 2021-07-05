set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
result = set2.difference(set1)
set1.update(result)
print(set1)
