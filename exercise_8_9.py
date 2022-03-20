from math import sqrt


def div_to_seven():
    #Я уверен, что есть более эффективное решение, но я до него не дошел :(
    return sum((2**i - i) % 7 == 0 for i in range(1000))


print(div_to_seven())  # 142


def is_in_fibonachi(n):
    # Натуральное число N является числом Фибоначчи тогда и только тогда, когда 5N^2 + 4 или 5N^2 - 4 является квадратом.
    # Определение с вики
    return True if sqrt(5 * (n ** 2) - 4) % 1 == 0 or sqrt(5 * (n ** 2) + 4) % 1 == 0 else False


print(is_in_fibonachi(5))  # True
print(is_in_fibonachi(200))  # False
print(is_in_fibonachi(75025))  # True

