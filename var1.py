import os
import random


def check_input(n: str) -> bool:
    return len(n) != NUMBERS and all(map(lambda x: x in DIGIT, n))


def player_to_player():
    num = ''
    print('Первый игрок загадывает число.')
    while check_input(num):
        num = input('Введите цифру:')
    os.system('clear')
    print('Цифра загадана')
    n = 1
    game = True
    while game:
        print(f'Второй игрок. {n} попытка')
        num1 = ''
        while check_input(num1):
            num1 = input('Введите цифру:')
        game, bull, cow = compare_answer(num, num1)
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


def compare_answer(n, n1):
    g, b, c = True, 0, 0
    for i in range(NUMBERS):
        if n1[i] == n[i]:
            b += 1
        elif n1[i] in n:
            c += 1
    if b == NUMBERS:
        g = False
    return g, b, c


def player_to_comp():
    num = ''
    print('Первый игрок загадывает число.')
    while check_input(num):
        num = input('Введите цифру:')
    os.system('clear')
    print('Цифра загадана')
    n = 1
    game = True
    options = set(map(str, range(10 ** NUMBERS)))
    while game:
        print(f'Второй игрок. {n} попытка')
        num1, options = gen_number(options)
        print(f'Цифра {num1}')
        game, bull, cow = compare_answer(num, num1)
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


def gen_number(option):
    n = random.choice(list(option))
    option -= set(n)
    return n, option


def comp_to_comp():
    num = random.choice(list(map(str, range(10 ** NUMBERS))))
    os.system('clear')
    print('Цифра загадана')
    n = 1
    game = True
    options = set(map(str, range(10 ** NUMBERS)))
    while game:
        print(f'Второй игрок. {n} попытка')
        num1, options = gen_number(options)
        print(f'Цифра {num1}')
        game, bull, cow = compare_answer(num, num1)
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


NUMBERS = 1
DIGIT = list(map(str, range(10)))
print(f"""
Игра 'Быки и коровы'
Первый игрок загадывает цифру из {NUMBERS} уникальных символов.
Варианты символов: {', '.join(DIGIT)}
Второй игрок отгадывает ее. 
Если цифра - правильная и стоит на своем месте - это бык.
Если цифра - правильная, но не своем месте - это корова.
Задача: угадать загаданную цифру.  
""")
op = True
while op:
    print('\n1. Игрок против игрока')
    print('2. Игрок против игрока')
    print('3. Игрок против игрока')
    answer = '0'
    while answer not in '123' or len(answer) != 1:
        answer = input('Введите вариант: ')
    if answer == '1':
        player_to_player()
    elif answer == '2':
        player_to_comp()
    else:
        comp_to_comp()
    an = ' '
    while an not in 'ДдНн':
        an = input('Ещё раз? (д/н) ')
    if an.lower() == 'н':
        op = False
        print('Доброго дня!')
    else:
        os.system('clear')
