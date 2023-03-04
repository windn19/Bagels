import os
import random


def player_to_player():
    num = ''
    print('Первый игрок загадывает число.')
    while len(num) != numbers and all(map(str.isdigit, num)):
        num = input('Введите цифру:')
    os.system('clear')
    print('Цифра загадана')
    n = 1
    game = True
    while game:
        print(f'Второй игрок. {n} попытка')
        num1 = ''
        while len(num1) != numbers and all(map(str.isdigit, num1)):
            num1 = input('Введите цифру:')
        game, bull, cow = compare_answer(num, num1)
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


def compare_answer(n, n1):
    g, b, c = True, 0, 0
    for i in range(numbers):
        if n1[i] == n[i]:
            b += 1
        elif n1[i] in n:
            c += 1
    if b == numbers:
        g = False
    return g, b, c


def player_to_comp():
    num = ''
    print('Первый игрок загадывает число.')
    while len(num) != numbers and all(map(str.isdigit, num)):
        num = input('Введите цифру:')
    os.system('clear')
    print('Цифра загадана')
    n = 1
    game = True
    options = set(map(str, range(10 ** numbers)))
    while game:
        print(f'Второй игрок. {n} попытка')
        num1, options = gen_number(options)
        print(f'Цифра {num1}')
        game, bull, cow = compare_answer(num, num1)
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


def gen_number(op):
    n = random.choice(list(op))
    op -= set(n)
    return n, op


def comp_to_comp():
    num = random.choice(list(map(str, range(10 ** numbers))))
    os.system('clear')
    print('Цифра загадана')
    n = 1
    game = True
    options = set(map(str, range(10 ** numbers)))
    while game:
        print(f'Второй игрок. {n} попытка')
        num1, options = gen_number(options)
        print(f'Цифра {num1}')
        game, bull, cow = compare_answer(num, num1)
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


numbers = 1
digit = list(map(str, range(10)))
print(f"""
Игра 'Быки и коровы'
Первый игрок загадывает цифру из {numbers} уникальных символов.
Варианты символов: {', '.join(digit)}
Второй игрок отгадывает ее. 
Если цифра - правильная и стоит на своем месте - это бык.
Если цифра - правильная, но не своем месте - это корова.
Задача: угадать загаданную цифру.  
""")
print('\n1. Игрок против игрока')
print('2. Игрок против компьютера')
print('3. Компьютер против компьютера')
answer = '0'
while answer not in '123' or len(answer) != 1:
    answer = input('Введите вариант: ')
if answer == '1':
    player_to_player()
elif answer == '2':
    player_to_comp()
else:
    comp_to_comp()

