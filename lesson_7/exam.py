"""Модуль вывовит список дата с таймаутом в 1 секунду"""
from functools import reduce

from beartype import beartype

# from datetime import datetime
# from time import sleep
#
#
# def sleep_time() -> str:
#     """Возврашает текущую дату в строке с таймаутом в 1 секунду"""
#     now_ = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
#     sleep(1)
#     return now_
#
#
# def range_number(n: int) -> list:
#     """Генератор списков возрашает список дат"""
#     data_list = [sleep_time() for _ in range(n)]
#     return data_list
#
#
# number = int(input('Введите число: '))
#
# print(range_number(number))
#
# print(range_number.__doc__)
# print(sleep_time.__doc__)

#
# def func(x):
#     return x * 2
#
# print(func(3))


# number = lambda x, y: x * (2 + y)
#
# print(number(3, 7))


# numbers = [1, 2, 3, 4, 5]
# # new_list = []
# #
# #
# # def func(data: list) -> None:
# #     for num in data:
# #         new_list.append(num ** 2)
# #
# #
# # func(numbers)
# # print(new_list)
#
#
# def func2(number: int) -> int:
#     return number ** 2
#
#
# numbers2 = map(func2, numbers)
# print(numbers2)
# print(type(numbers2))
# print(list(numbers2))
# [1, 4, 9, 16, 25]

# str_name = ['4', '5', '6', '7', ' 8']
# numbers_int = map(int, str_name)
# list_int = list(numbers_int)
# print(list_int)
# number_float = map(float, list_int)
# print(list(number_float))
#
# names = ['Nikolay', 'Aleksandr', 'Olga']
# names_str = map(len, names)
# # print(names_str.__next__())
# print(list(names_str))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# def fileter_num(num: int) -> bool:
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#     # return num % 2 == 0
#
# my_filter = filter(fileter_num, numbers)
# # print(my_filter.__next__())
#
# print('type', type(my_filter))
# print('type', list(my_filter))

# new_list = list(filter(lambda x: x % 2 == 0, numbers))
# print(new_list)
#
# numbers = [1]
#
# @beartype
# def custom_sum(first: int, second: int) -> int:
#
#     return first + second
#
#
# result = reduce(custom_sum, numbers)
# print(type(result))
# print(result)


# @beartype
# def custom_sum(first: int, second: int) -> int:
#     """Сложение данных"""
#
#     return first + second
#
# print(custom_sum("1","2"))

from beartype import beartype

@beartype
def analyze_the_string(text: str) -> float | str:
    """Определяю, содержатся ли во входящей строке цифры
    и, в зависимости от результата, привожу к float"""
    d = text.isdigit()

    b = text.replace(',', '.')
    if d is True:
        return int(a)
    elif '.' in text:
        return float(b)
    elif text[0] == '-':
        return float(b)
    else:
        return 'Некорректная строка'

a = '-2,4'

print(analyze_the_string(a))