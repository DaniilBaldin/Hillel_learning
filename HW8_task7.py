test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_num = 0
max_num = 0
for i in range(1, len(test_list)):
    if test_list[i] > test_list[max_num]:
        max_num = i
    if test_list[i] < test_list[min_num]:
        min_num = i
test_list[min_num], test_list[max_num] = test_list[max_num], test_list[min_num]
print(' '.join([str(i) for i in test_list]))
