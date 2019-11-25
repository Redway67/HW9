"""
Класс Player
"""
from classes.card import Card, CARD_WIDTH, CARD_HEIGHT, CARD_FILLED, CARD_QUANTITY

# типы игроков
types_of_players = {1: 'Человек', 2: 'Компьютер'}


class Player:

    def __init__(self, name='Неизвестный', who=1, dim_card=(CARD_WIDTH, CARD_HEIGHT, CARD_FILLED, CARD_QUANTITY)):
        self.name = name
        self.who = types_of_players[who]
        self.dim_card = dim_card
        self.cards = {}

    def show_cards(self):
        print('Карточка')
        for i in range(0, self.dim_card[1]):
            print('*' * self.dim_card[0], end=' ')
            print('')

    def move_on(self):
        print('Хожу')
