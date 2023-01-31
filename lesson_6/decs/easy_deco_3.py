"""Простейший декоратор-функция"""

import time
import requests


def decorator(func):
    """Сам декоратор"""

    # def wrapper(u):
    def wrapper(*args, **kwargs):  # если передаем аргумет то и обязаны его принять
        """Обертка"""
        start = time.time()
        return_value = func(*args, **kwargs)
        # return_value = func(url)
        # return_value = func(args[0])
        end = time.time()
        print(f'Отправлен запрос на адрес {kwargs.get("url")}. '
              f'Время выполнения: {round(end - start, 2)} секунд')
        # обертка может возвращать и некий результат
        return return_value

    return wrapper


@decorator
def get_wp(url="https://ya.ru"):  # передача аргумента
    """Делаем запрос"""
    res = requests.get(url)
    return res


print(get_wp(url='https://google.com'))
