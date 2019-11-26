"""
Класс Game
"""

from classes.player import Player
from classes.bag import Bag

QUANTITY_PLAYERS = 2  # по умолчанию игроков два


class Game:

    def __init__(self):
        self.players = [Player(i) for i in range(1, QUANTITY_PLAYERS + 1)]
        self.bag = Bag()
        self.is_run = True

    # Вытаскиваем бочонок
    def get_barrel(self):
        barrel = 0
        print('Кручу-верчу запутать хочу!!')
        return barrel

    # Старт игры
    def start(self):
        print('Рассказываем правила ...')
        print('Поехали!')

    # Финиш игры
    def finish(self):
        print(f'Победитель')
