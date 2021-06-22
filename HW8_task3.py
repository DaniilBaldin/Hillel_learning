test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Enter the number: ')
a = int(input())
if a in test_list:
    print(f'Yes, {a} is in the list!')
else:
    print(f'No, {a} is not in the list!')
