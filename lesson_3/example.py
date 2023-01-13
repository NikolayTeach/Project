# text = 'HELLO'
# print(len(text))


# days = 10
# rate = 200
#
# text = f"Иванов И.И получает {rate*days} его ставка : {rate} и он 'hi' \"\" отработал дней: {days}"
#
# print(text)


# number1 = 7
# number2 = 2
# print(number1 % number2)


# number1 = 5
# number2 = 2
# print(number1 ** number2)

# number1 = 12
# number2 = 5
# print(number1 // number2)


# number1 = 6
# number2 = 6
# print(number1 <= number2)

#Неизмен
# str_ = 'hi'
# str_2 = 'hi'
# str_3 = 'hi'
# int_ = 1
# int_2 = 1
# float_ = 2.0
# float_2 = 2.0
# bool_ = True
# bool_2 = True
#
# print(id(bool_))
# print(id(bool_2))


#Измен
# list_ = []
# list_.append(1)
# list_.append(2)
# list_.insert(0, 5)
# print(list_)
# list_.pop(2)
# list_.sort(reverse=True)
# list_.clear()
#
# print(list_)

# list_1 = [1, 2, 3, 4, 5]
# list_2 = list_1.copy()
# list_2.append(17)
#
# print(list_1, list_2)
#
# print(id(list_1), id(list_2))

#Неизмен
# tuple_ = (1, 2, 3, 4, 4)
# print(tuple_.count(4))
# print(tuple_.index(4))
#
# list_2 = list(tuple_)
# list_2.append(10)
# print(list_2)
# tuple_2 = tuple(list_2)
# print(tuple_2)


# frozenset_ = frozenset((1,))
# print(frozenset_)
#
# text = bytes('привет'.encode())
# # bytes_ = b'test'
# print(type(text))
# print(text)

# list_2 = ['hi', 77, 3, 3, 89]

#Измен

# set_ = set(list_2)
# set_.add(1)
# set_.add(3)
# set_.add(5)
# set_.add(2)
# print(set_)
# print(set_)
# print(set_)
# print(set_)
# print(set_)
# print(set_)
# print(set_)


# dict_ = {'privet': 2}
#
# dict_['hi'] = 1
# print(dict_)
# dict_['hi'] = 3
# print(dict_)

#Пример про потерю hash  суммы

# dict_ = {'hi': 1}
# dict_24 = {'hi': [1, 2, 34], 'key': '3'}
# dict_2 = {'hi': {'g': 3}}
#
# print(dict_['hi'].__hash__)
# print(dict_24['key'].__hash__)
# print(dict_24['hi'].__hash__)
# print(dict_2['hi'].__hash__)
a = dict([(1, 1), (2, 4)])
print(a)


# TODO тест