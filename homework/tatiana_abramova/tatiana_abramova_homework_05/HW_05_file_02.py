result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

colon_index1 = result1.index(':')
colon_index2 = result2.index(':')
colon_index3 = result3.index(':')

number1 = int(result1[colon_index1 + 2:]) + 10
number2 = int(result2[colon_index2 + 2:]) + 10
number3 = int(result3[colon_index3 + 2:]) + 10

print(number1)
print(number2)
print(number3)
