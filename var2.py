import os
import random
import string


def check_input(n: str) -> bool:
    if n == '' or len(n) > NUMBERS:
        return True
    if len(n) < NUMBERS:
        n = '0' * (NUMBERS - len(n)) + n
    for char in n:
        if char not in DIGIT:
            return True
    return False


def player_to_player() -> None:
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
        print(f"В вашем слове: {bull} быков и {cow} коров")
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


def compare_answer(n: str, n1: str) -> tuple:
    g, b, c = True, 0, 0
    n = n if len(n) >= NUMBERS else '0' * (NUMBERS-len(n)) + n
    n1 = n1 if len(n1) >= NUMBERS else '0' * (NUMBERS-len(n1)) + n1
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
    options = set(prepare_option())
    num1, bull, cow = '', 0, 0
    while game:
        print(f'Второй игрок. {n} попытка')
        num1, options = gen_number(options, num1, bull, cow)
        print(f'Цифра {num1}')
        game, bull, cow = compare_answer(num, num1)
        print(f"В вашем слове: {bull} быков и {cow} коров")
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


def gen_number(option, num: str, b: int, c: int) -> tuple:
    if num != '':
        opt = set()
        if b or c:
            for nn, i in enumerate(num):
                for it in list(option):
                    it = it if len(it) > 1 else '0' * (NUMBERS-len(it)) + it
                    if b and it[nn] == i:
                        opt.add(it)
                    if c and i in it:
                        opt.add(it)
            option = opt
        else:
            for char in list(num):
                for it in list(option):
                    if char in it:
                        opt.add(it)
            option -= opt
    print(option)
    n = random.choice(list(option))
    option.remove(n)
    return n, option


def comp_to_comp():
    num = random.choice(prepare_option())
    num = num if len(num) > 1 else '0' * (NUMBERS-1) + num
    os.system('clear')
    print(f'Цифра загадана - {num}')
    n = 1
    game = True
    num1, bull, cow = '', 0, 0
    options = set(prepare_option())
    while game:
        print(f'Второй игрок. {n} попытка')
        num1, options = gen_number(options, num1, bull, cow)
        print(f'Цифра {num1}')
        game, bull, cow = compare_answer(num, num1)
        print(f"В вашем слове: {bull} быков и {cow} коров")
        n += 1
        print('Неверно!' if game else 'Цифра угадана. Игра окончена')


def prepare_option() -> list:
    option = []
    for n in map(str, range(10 ** NUMBERS)):
        if len(n) < NUMBERS:
            n = '0' * (NUMBERS - len(n)) + n
        if len(set(n)) == len(list(n)):
            option.append(n)
    # option = list(filter(lambda x: len(set(x)) == len(list(x)), map(str, range(10 ** NUMBERS))))
    return option


NUMBERS = 3
DIGIT = string.digits
print(DIGIT)
# exit()
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
    print('2. Игрок против компьютера')
    print('3. Компьютер против компьютера')
    print('4. Выход')
    answer = '0'
    while answer not in '1234' or len(answer) != 1:
        answer = input('Введите вариант: ')
    if answer == '1':
        player_to_player()
    elif answer == '2':
        player_to_comp()
    elif answer == '3':
        comp_to_comp()
    else:
        op = False
        continue
    an = ' '
    while an not in 'ДдНн':
        an = input('Ещё раз? (д/н) ')
    if an.lower() == 'н':
        op = False
    else:
        os.system('clear')
else:
    print('Доброго дня!')
