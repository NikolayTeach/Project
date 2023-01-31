"""Простейший декоратор-функция"""

import time
import requests

def decorator(func):
    """Сам декоратор"""
    def wrapper():
        """Обертка"""
        start = time.time()
        func()
        end = time.time()
        #Получаем дельту
        print(f'Время выполнения исходной ф-ции: {round(end-start, 2)} секунд')
    return wrapper


@decorator
def get_wp1():
    """
    получаем ответ сервера
    200 - запрос успешно обработан
    """
    print('Выполняем расчет yandex')
    res = requests.get('https://ya.ru')
    return res

@decorator
def get_wp():
    """
    получаем ответ сервера
    200 - запрос успешно обработан
    """
    print('Выполняем расчет google')
    res = requests.get('https://google.com')
    return res


get_wp()
get_wp1()