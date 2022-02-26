def find_three_min_nums(arr):

    if len(arr) <= 3: #Защита от дурака
        return arr

    return sorted(arr)[:3] #Сортируем и берем первые 3 числа


print(find_three_min_nums([2, 1, 6, 1, 0])) # [0, 1, 1]
print(find_three_min_nums([2, 0])) # [2, 0]
print(find_three_min_nums([0, 0, 10, 50, 100, 3])) # [0, 0, 3]