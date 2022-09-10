# def a_function():
#     print("You just created a function!")
# a_function()
#
#
# def empty_functyon():
#     pass
# empty_functyon()
#
#
# def listsum():
#     sum = 0
#     for i in range(10):
#         sum += i
#     print(sum)
# listsum()


# def ad(a, b):
#     return a + b
# print(ad(1, 2))
#
#
#
# total = ad(b=4, a=5)
# print(total)



# # ОПРЕДЕЛЕНИЕ ФУНКЦИИ
# def sayHello():
#     print('Hello')
#     print('World')
#     print('and everybody')
#
# sayHello()
# print('pause')
# sayHello()


# def kei(d=4, a=5):      # обьявляем функцию с ключевым аргументом d и a
#     return a+d          # складываем значения
# print(kei())            # вызываем функцию с аргументом по умолчанию
# print(kei(d=2, a=1))    # вызываем функцию меняя аргументы на нужные нам


# def mix(a, b=2, c=3):    # обьявляе функцию где a - обычный аргумент, b и c ключевые аргументы
#     return a + b + c     # складываем значения
# print(mix(1, b=4, c=5))  # вызываем функцию, задаём значения обычному аргументу и меняем значения ключевым аргументом
# print(mix(1))            # вызываем функцию, задаём значения обычному аргументу


# def many(*args, **kwargs):                 #
#     print(args)
#     print(kwargs)
# many(1, 2, 3,name="Mike", job="programtr")



# def function_a():     # обьявляем функцию
#     global a          # делаем a глобальной
#     a = 1             # обьявляем переменную
#     b = 2             # обьявляем переменную
#     return a + b      # складываем значения
#
# def function_b():     # обьявляем функцию
#     c = 3             # обьявляем переменную
#     return a + c      # складываем значения
# print(function_a())   # вызываем функцию a и делаем переменную a в глобальную
# print(function_b())   # вызываем функцмю b и используем глобальную переменную


# def is_year_leap(year):                                        # объявляем функцию
#     return year % 4 ==0 and year % 100 != 0 or year % 400 == 0 # проверяем год на высокостность
# print(is_year_leap(int(input('Введите год'))))                 # вводим год с клавиатуры


# import math                                           # импортируем библиотеку math
# def square(a):                                        # объявляем функцию
#     p = 4 * a                                         # считаем периметр, площадь и диагональ квадрата по условию задачи
#     s = a **2
#     d = math.sqrt(2) * a
#     return p, s, d                                    # возвращаем значение
# print(square(int(input('Введите сторону квадрата:'))))# вызываем функцию и вводим число из клавиатуры


# def season(num):                  # объявляем функцию
#     if num == 12 or 1 <= num <= 2:# выбираем какой месяц к какой поре года относится
#         print("Зима")
#     elif 3 <= num <= 5:
#         print("Весна")
#     elif 6 <= num <= 8:
#         print("Лето")
#     elif 9 <= num <= 11:
#         print("Осень")
#     else:
#         print("Неверно введён номер месяц!")
#
# season(int(input("Введите номер месяца")))


# def is_prime(chislo):                                                       # объявляем функцию
# return chislo % 2 ==0 or chislo % 3 ==0 or chislo % 4 ==0 or chislo % 5 ==0 # проверяем является ли число простым. Если число простое, выводим folse, иначе true
# print(is_prime(7))                                                          # вызываем функцию


# import random                                      # импортируем библиотеку random
#
# def elem():                                        # объявляем функцию
#     a = [random.randint(1, 100) for i in range(10)]# генерируем список
#     s = 0
#     for i in a:                                    # складываем элементы списка
#         s += i                                     # складываем элементы списка
#     return a , s , s/10                            # return - возвращаем переменные
# print(elem())                                      # вызыва


# def factorial(n):                   # объявляем функцию
#     if n != 0:                      # проверяем является ли число n нулём
#         return n * factorial(n - 1) # выщитываем факториал
#     else:                           # возвращаем 1 если факториал равен 0
#         return 1                    #
# print(factorial(5))                 # вызываем функцию


# def add(a, b):                      # объявляем функцию
#     return a + b                    # возвращаем сумму
# variable = add(1, 2)                # сохраняем значение в переменной
# print(variable)                     #
# print(add(5, 10))                   # вызов функции



# def func(x): return x               #
# a1 = func
# a2 = a1
# print(a2(10))
# print(a1(7))



# product = lambda x, y: x * y
# print(product(2, 3))
# print(type(product))


# power = lambda x=1, y=2: x **y
# square = power
# print(square(5))



# def mul(a):
#     def helper(b):
#         return a * b
#     return helper
# print(mul(3)(2))
#
# three_mul = mul(3)
# print(three_mul(5))



# def simple_decore(fn):
#     print("Start function")
#     fn()
#     print("Stop function")
#
# @simple_decore
# def first_test():
#     print("Test function 1")
#
# @simple_decore
# def second_test():
#     print("Test function 2")


# first_test_wrapper = simple_decore(first_test)
# second_test_wrapper = simple_decore(second_test)


# def digits(n):
#     i = 0
#     while n > 0:
#         n = n // 10
#         i += 1
#     return i
#
# num = abs(int(input('Введите число:')))
# print('Колличество разрядов:', digits(num))



def convert(seconds):
    days = seconds // (24 * 3600)
    print(days)
    seconds = seconds % (24 * 3600)
    print(seconds)
    hours = seconds // 3600
    print(hours)
    seconds = seconds % 3600
    print(seconds)
    minutes = seconds // 60
    print(minutes)
    seconds = seconds % 60
    print(seconds)
    print(f'{days}:{hours}:{minutes}:{seconds}')
convert(3467896)
