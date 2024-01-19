# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм

n = int(input('Put your number: '))

print('Structure way:')
for i in range(1, n + 1):
    print(f'\nThe multiplication table for {i}')
    for k in range(1, 10):
        print(f'{i} * {k} = {i * k}')

print('\Structural + procedural:')


def get_multiplication_table(j):
    for item in range(1, j + 1):
        print(f'\nThe multiplication table for {item}')
        for i in range(1, 10):
            print(f'{item} * {i} = {item * i}')


get_multiplication_table(n)

print('\nDeclarative way:')
print(''.join([f'{i} * {k} = {i * k}\n' for i in range(1, n + 1) for k in range(1, 10)]))
