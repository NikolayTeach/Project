import sys

# from replit import clear
import os
import subprocess
import timeit
from typing import Generator, Union

# print('Код до очистки экрана')
# # clear()
# print('Код ПОСЛЕ очистки экрана','\n')
#
# print('Код до очистки экрана')
# # os.system('cls') #on Windows System
# print('Код ПОСЛЕ очистки экрана','\n')
#
# print('Код до очистки экрана')
# # subprocess.run('cls', shell=True)
# print('Код ПОСЛЕ очистки экрана')

# print('\033[F\033[K', end='')


# import random
#
# number = random.randint(1, 100)
# while True:
#     user = int(input("Угадай число от 1 до 100 "))
#     if user > number:
#         print("Число должно быть меньшь!")
#     elif user < number:
#         print('Число должно быть больше')
#     else:
#         print(f'Вы угадали это число {number}')
#         break


# # попробуем измерять скорость выполнения объявленных функций
# def my_function_1():  # функция, считающая сумму всех чисел от 0 до 100 с использованием цикла for
#     total = 0
#     for i in range(100 + 1):
#         total += i
#     return total
#
#
# def my_function_2():  # функция, считающая сумму всех чисел от 0 до 100 с использованием цикла while
#     total = 0
#     counter = 0
#     while counter < 100:
#         counter += 1
#         total += counter
#     return total
#
#
# print(my_function_1(), my_function_2())  # как видим, обе функции делают то же самое
# # измеряем время выполнения каждой функции, узнаем какой цикл будет работать быстрее
# print('Цикл for: ', timeit.timeit(stmt='my_function_1()', number=10000, globals=globals()))
# print('Цикл while: ', timeit.timeit(stmt='my_function_2()', number=10000, globals=globals()))
# # можем сделать вывод, что цикл for работает быстрее


# number = 0
#
# speed_for = \
# """
# result_for = 0
# for num in range(1, number+1):
#     result_for += num**2
# """
# print(timeit.timeit(speed_for, globals=globals()))

# import keyword
#
# print(keyword.kwlist)

# def func(a, b, c=3):
#
#     return a + b + c
#
# #
# # print(func())
#
#
#
# result = func(1,2,8)
# # if result:
# #     print(result+1)
# print(result)

# print(result + 1)

# def func(*args, **kwargs):
#     for i in args:
#         print(i)
#     for k,v in kwargs.items():
#         print(k,v)
#
# func(1, 2, 3, 4, 5, 6,id=5,client='Nikolai',day="Monday")


# def func(number1, number2):
#
#     return number1 ** number2
#
# c = func(number1=50,number2=2)
# print(c)


# def func(**kwargs):
#     keys = []
#     values = []
#
#     for k, v in kwargs.items():
#         print(k, v)
#         keys.append(k)
#         values.append(v)
#     return keys, values
#
#
# keys, values = func(a=5)
#
# print('Параметры', keys, values)


# c = 0
#
#
# def func():
#     global c
#     c = 20
#     print(c)
#
#
# func()
# c += 1
# print(c)


#
# c = 0
# print(id(c))

# def func(rate, days):
#     salary = rate*days
#     return salary
#
# c = func(100,30)
#
# print(id(c))


# c = 0
#
# def func(c):
#     c+=1
#     return c
#
# print(func(2))

# def func2() -> Generator:
#     yield 2
#
# a = type(func2())
# print(a)

# @beartype
# def func(name: str = "world") -> Union[str, int]:
#     return 'Hello' + name
#
# print(func(name=1))

a = range(1, 15)
random_list = []
for i in a:
    if i % 2 == 0:
        random_list.append(i)


# random_list = [i*7 for i in range(1, 15) if i % 2 == 0]
# print(random_list)
