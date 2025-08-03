"""
Напишите программу. Есть две переменные, salary и bonus. Salary - int, bonus - bool.
Спросите у пользователя salary. А bonus пусть назначается рандомом.

Если bonus - true, то к salary должен быть добавлен рандомный бонус.

Примеры результатов:

10000, True - '$10255'
25000, False - '$25000'
600, True - '$3785'
"""

import random

def calculate_final_salary():
    salary = int(input("Введите значение salary: "))
    bonus = random.choice([True, False])
    if bonus:
        random_bonus = random.randint(0, 1000)
        final_salary = salary + random_bonus
    else:
        final_salary = salary

    return f"{salary}, {bonus} - '${final_salary}'"

result = calculate_final_salary()
print(result)
