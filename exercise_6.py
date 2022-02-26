def find_three_min_nums(arr):
    res = []

    if len(arr) <= 3: #Защита от дурака
        return arr

    for i in range(3): #Находим 3 минимальных числа и добавляем их в результат
        min_num = min(arr)
        res.append(min_num)
        arr.remove(min_num)

        if len(res) == 3:
            return res


print(find_three_min_nums([2, 1, 6, 1, 0])) # [0, 1, 1]
print(find_three_min_nums([2, 0])) # [2, 0]
print(find_three_min_nums([0, 0, 10, 50, 100, 3])) # [0, 0, 3]