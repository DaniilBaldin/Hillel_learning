test_list = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
print('Enter the searched number: ')
a = int(input())
if a in test_list:
    print(f'Yes, there is {a} in the list!')
else:
    print(f'There is no {a} in the list!')
