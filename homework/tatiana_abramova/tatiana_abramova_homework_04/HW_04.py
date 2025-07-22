my_dict = {
    'tuple': (11, 12, 13, 14, 15, 16),
    'list': ['a', 'b', 30, 40, True],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {'A', 100, 200, 300, 400, 500}
}

last_tuple_element = my_dict['tuple'][-1]
print(f'Последний элемент кортежа внутри словаря: {last_tuple_element}')

my_dict['list'].append(50)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 6
my_dict['dict'].pop('a')

my_dict['set'].add('B')
my_dict['set'].pop()

print(my_dict)
print("Итоговый словарь:", my_dict)
