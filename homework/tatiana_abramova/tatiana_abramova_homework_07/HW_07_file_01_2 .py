number = 5

while True:
    user_number = int(input('Введите цифру от 0 до 9: '))
    if user_number == number:
        break
    else:
        print("Попробуй снова")

print('Поздравляю! Вы угадали!')
