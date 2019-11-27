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
        name_player = input(f'Введите имя (по умолчанию Неизвестный {number}) :')
        self.name = (name_player if name_player else 'Неизвестный ' + str(number))
        # TODO: проверить имя на уникальность

        # присваиваем тип игрока
        for t in range(0, len(types_of_players)):
            print(f'тип {types_of_players[t]} - {t} ')
        try:
            who = int(input(f'Введите тип игрока (по умолчанию тип {types_of_players[0]}) :'))
            if who > len(types_of_players): raise ValueError
        except ValueError:
            who = 0
            print(f'Ошибка! Установлен тип по умолчанию {types_of_players[0]}')
        self.who = who

        # заполняем карточку игрока
        self.cards = [Card(i) for i in range(0, QUANTITY_CARDS)]

    def show_cards(self):
        for i in range(0, len(self.cards)):
            self.cards[i].show_card()

    def move_on(self):
        print('Хожу')
