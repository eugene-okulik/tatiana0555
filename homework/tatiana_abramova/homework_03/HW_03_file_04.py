# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь


from math import sqrt

leg1 = 3
leg2 = 4
hypotenuse = sqrt(leg1 ** 2 + leg2 ** 2)
area = (leg1 * leg2) / 2
print('Гипотенуза прямоугольного треугольника равна', hypotenuse)
print('Площадь прямоугольного треугольника равна', area)
