from math import *       # импортируем библиотеку math,после import пишем имя функции (pow)  или *
a = float(input("введите угол а в градусах"))
b = float(input("введите угол b в градусах"))
y = float(input("введите угол y в градусах"))
a = radians(a)           # переводим в нужную единицу измерения в радиан
b = radians(b)           # переводим в нужную единицу измерения в радиан
y = radians(y)           # переводим в нужную единицу измерения в радиан
f = pow(4, -1) * ( sin(a + b - y) + sin(b + y - a) + sin(y + a -b) - sin(a + b + y))
print(f)