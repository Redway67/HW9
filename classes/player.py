"""
Класс Player
"""
from classes.card import Card

QUANTITY_CARDS = 1  # по умолчанию карточек 1

# типы игроков
types_of_players = {0: 'Человек', 1: 'Компьютер'}


class Player:

    def __init__(self, number=1):
        self.number = number

        # присваиваем имя игроку
        name_player = input(f'Введите имя (по умолчанию Неизвестный {number}) :')
        self.name = (name_player if name_player else 'Неизвестный ' + str(number))
        # TODO: проверить имя на уникальность

        # присваиваем тип игрока
        for t in range(0, len(types_of_players)):
            print(f'тип {types_of_players[t]} - {t} ')
        try:
            who = int(input(f'Введите тип игрока (по умолчанию тип {types_of_players[0]}) :'))
        except ValueError:
            who = 0
            print(f'Вводить нужно цифру! Установлен тип по умолчанию {types_of_players[0]}')
        self.who = who
        # TODO: проверить на выход из диапозона

        self.cards = [Card(i) for i in range(1, QUANTITY_CARDS + 1)]



    def move_on(self):
        print('Хожу')
