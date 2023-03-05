# python3.10
import os
import string
import sys


class Game:
    NUMBERS = 1
    COMPOUND = string.digits

    def run(self):
        print(f"""
        Игра 'Быки и коровы'
        Первый игрок загадывает цифру из {self.NUMBERS} уникальных символов.
        Варианты символов: {', '.join(self.COMPOUND)}
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
            print('4. Компьютер против человека')
            print('5. Выход')
            answer = '0'
            while answer not in '12345' or len(answer) != 1:
                answer = input('Введите вариант: ')
            match answer:
                case '1':
                    # player_to_player()
                    pass
                case '2':
                    # player_to_comp()
                    # todo игрок загадывает компьютер отгадывает
                    pass
                case '3':
                    # comp_to_comp()
                    # todo компьютер загадывает число и компьютер отгадывает
                    pass
                case '4':
                    # todo ? компьютер загадывает, а человек отгадывает
                    pass
                case _:
                    op = False
                    continue
            an = ' '
            while an not in 'ДдНн':
                an = input('Ещё раз? (д/н) ')
            if an.lower() == 'н':
                op = False
            else:
                os.system('cls' if sys.platform.startswith('win') else 'clear')
        else:
            print('Доброго дня!')

    @classmethod
    def check_input(cls, n: str) -> bool:
        # todo проверка ввода пользователя
        pass

    def gen_number(self, option: set) -> tuple:
        # todo генерация номера для проверки
        pass

    def prepare_option(self) -> list:  # set?
        # todo подготовка все возможных вариантов
        pass


class Player:
    # todo общий класс для игроков,
    # todo ? абстрактный класс - общие методы загадывание цифры и ввод результата
    def compare_answer(self, n, n1):
        # todo сравнение двух ответов - быки - коровы
        pass


class HumanPlayer(Player):
    # todo шаг и определение числа
    pass


class CompPlayer(Player):
    # todo шаг и определение числа
    pass
