import timeit

# a = input('Введеная строка: ')
#
# b = a[0::2]
# c = a[1::2]
# print(b)
# print(c)
# #
# print(a.strip(), end='\n\n\n')
#
# print(b, c, sep='     ', end='!!!')


# import __hello__
# import this
# print(__hello__.main())
# print(this)


# spam = 'Spam'
# print(spam)
#
# spam1, ham = ('yum', 'Yum')
# print(spam1, ham)
#
# list1, list2 = ['yum', 'Yum']
# print(list1, list2)
#
# a, b, c, d = 'spam'
# print(a, b, c, d)
#
# a, *b = 'spam'
# print(a, b)
#
# spam = hum = 'hello'
#
# print(spam, hum)
# spams = 5
#
# spams += 42
# print(spams)
#
# a = 1
# b = 2
# print(a, b)
#
# a, b = b, a
# print(a, b)
#
#
# first_name = input('Enter your first name ')
# last_name = input('Enter your last name ')
#
# print("Hello {first_name} {last_name}".format(first_name=first_name, last_name=last_name))
# print(f"Hello {first_name} {last_name}")

# a = '1'
# b = '1'
#
# print(id(a), id(b))
# print(a is not b)
#
#
# list_a = [1, 2, 3, 4, 5]
#
# c = 30
#
# print(c in list_a)
#
#
# # print(not False or True and False)
# # print(True and False)
#
# a = 111111111111111
# b = 111111111111111
# print(id(a))
# print(id(b))


# print(timeit.timeit("x = 2 + 2"))
# print(timeit.timeit("x = sum([1, 2, 100, 200, 500])"))

# a = [1, 2, 3, 4, 5, 6]
#
# i = 0
#
#
# while True:
#     if len(a) == i:
#
#         break
#
#     if i == 2:
#         i += 1
#         continue
#
#     print(a[i])
#
#     i += 1

# i = 0
#
# while i < 10:
#     print(i)
#     i += 1
#
# else:
#     print('итератор отработал')


# a = [1, 2, 3, 4]
# b = []
# c = 5
# for _ in a:
#     print(id(c))
#
# else:
#     print(b)


# a = {'a': 1, 'b': 2, 'c': 3}
#
# for _, v in a.items():
#     print(v)

# a = int(input('number one '))
#
# b = int(input('number two '))
#
# c = 0
#
# if a > 10:
#     c = a
# else:
#     c = b
# print(c)
#
# c = a if a > 10 else b

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
e = []
for i in a:
    for c in b:
        e.append(i*c)

print(e)

