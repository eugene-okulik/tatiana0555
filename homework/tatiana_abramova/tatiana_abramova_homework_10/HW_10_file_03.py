"""Задание на декораторы 3
Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами
(числа и операция передаются в аргументы функции). Функция выглядит примерно так:

def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif .....
Программа спрашивает у пользователя 2 числа (вне функции)

Создайте декоратор, который декорирует функцию calc и управляет тем, какая операция будет произведена:
если числа равны, то функция calc вызывается с операцией сложения этих чисел
если первое больше второго, то происходит вычитание второго из певрого
если второе больше первого - деление первого на второе
если одно из чисел отрицательное - умножение
"""


def operation_decorator(func):
    def wrapper(num1, num2):
        if num1 == num2:
            return func(num1, num2, '+')
        elif num1 > num2:
            return func(num1, num2, '-')
        elif num2 > num1:
            return func(num1, num2, '/')
        elif num1 < 0 or num2 < 0:
            return func(num1, num2, '*')
    return wrapper


@operation_decorator
def calc(first, second, operation):
    try:
        if operation == '+':
            return first + second
        elif operation == "-":
            return first - second
        elif operation == "*":
            return first * second
        elif operation == "/":
            return first / second
    except ZeroDivisionError:
        return "Ошибка: деление на ноль невозможно."


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

result = calc(first_number, second_number)
print("Результат:", result)
