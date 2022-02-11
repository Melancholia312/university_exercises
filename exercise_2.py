import random

'''Функция кастомной сортировки'''
def my_sort(arr):

    '''Если массив состоит из одного элемента, то мы его просто возвращаем'''
    if len(arr) <= 1:
        return arr

    '''Выбираем стартовое число относительно которого будем сортировать'''
    start_elem = arr[0]
    '''Все числа, которые меньше стартового отправляются влево'''
    left = list(filter(lambda x: x < start_elem, arr))
    '''Все числа равные стартовому записываются в массив, который уже не нужно сортировать. Мы его просто возвращаем'''
    center = list(filter(lambda x: x == start_elem, arr))
    '''Все числа, которые больше стартового отправляются вправо'''
    right = list(filter(lambda x: x > start_elem, arr))

    '''Соединяем наши массивы и вызываем функцию сортировки рекурсивно, чтобы отсортировать правые и левые части'''
    return my_sort(left) + center + my_sort(right)

'''Делаем случайные массивы в качестве входных данных'''
first_arr = [random.randint(1,25) for i in range(10)]
second_arr = [random.randint(1,25) for j in range(10)]

print(my_sort(first_arr+second_arr))