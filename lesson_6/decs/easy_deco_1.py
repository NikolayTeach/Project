"""Простейший декоратор-функция"""

import time


def decorator(func):
    """Сам декоратор"""
    def wrapper():
        """Обертка"""
        print('Сейчас выполняется функция-обёртка')
        time.sleep(2)
        print(f'Это просто ссылка на экземпляр оборачиваемой функции: {func}')
        time.sleep(2)
        print('Выполняем оборачиваемую (исходную) функцию...')
        time.sleep(2)
        test = func()#Обязательно ли вызывать функцию?
        time.sleep(2)
        print('Выходим из обёртки')
        return test  #обязателен ли тут возврат?
        # обертка может ничего не возвращать
    return wrapper





@decorator #= decorator(some_text)
def some_text():
    """Какая-то логика"""
    print('вычисления')
    return "Возврат"



print(some_text())












# some_text = decorator(some_text)
# print(some_text())
