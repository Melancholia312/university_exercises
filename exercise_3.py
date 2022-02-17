import re


def add_nums_with_type_string(string):

    numbers_arr = re.split(r'[-+]', string) #Отделяем числа от знаков

    if not len(numbers_arr) >= 2: #Проверяем, что на вход нам пришло минимум 2 числа
        return None

    result = int(numbers_arr[0]) #Заносим первое число в список для последующего сложения
    pluses_and_minuses = list(filter(lambda num: num in ['+', '-'], string)) #Отделяем знаки от чисел

    for num, sign in zip(numbers_arr[1:], pluses_and_minuses):
        result += int(sign+num) #Конкатенируем знак с числом и преобразуем в int

    return result


print(add_nums_with_type_string('1+2+3-6')) # 0
print(add_nums_with_type_string('1+2+3+6-10')) # 2
print(add_nums_with_type_string('1000-1001')) # -1
print(add_nums_with_type_string('100')) # None

