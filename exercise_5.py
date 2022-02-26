def find_num_in_all_ars(arr1, arr2, arr3):
    for num in arr1: #Просто проверяем циклом наличие элемента во всех 3-ех массивах...
        if num in arr1 and \
           num in arr2 and \
           num in arr3:

            return num

    return None


first_arr = [1, 2, 3, 4, 5]
second_arr = [4, 5, 7, 8]
third_arr = [5, 7, 8, 9, 10]

first_arr_2 = [1, 2, 3, 4, 5]
second_arr_2 = [5, 6, 7, 8]
third_arr_2 = [7, 8, 9, 10]

first_arr_3 = [1, 2, 3, 4, 5]
second_arr_3 = [1, 5, 6, 7, 8]
third_arr_3 = [1]

print(find_num_in_all_ars(first_arr, second_arr, third_arr)) #5
print(find_num_in_all_ars(first_arr_2, second_arr_2, third_arr_2)) #None
print(find_num_in_all_ars(first_arr_3, second_arr_3, third_arr_3)) #1