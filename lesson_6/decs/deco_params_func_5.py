"""Простейший декоратор-функция с параметром"""
#Засыпаем на 10 секунд
import time

#функция ловушка
def sleep(timeout):
    """Внешняя функция (формально - декоратор)"""
    #декоратор всегда должен принимать на вход функцию
    def decorator(func):
        """Сам декоратор"""
        def decorated(*args, **kwargs):
            """Обертка"""

            time.sleep(timeout)
            res = func(*args, **kwargs)

            print(f'Функция {func.__name__} зависла')
            return res
        return decorated
    return decorator


@sleep(2)
def factorial(param):
    """Вычисляем факториал"""
    if param <= 1:
        return 1
    else:
        return param * factorial(param - 1)



print(factorial(5)) #вызов в сахром

#
# without_sagest = sleep(10)(factorial)
# print(without_sagest)