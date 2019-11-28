"""
Класс Game
"""
import random
from classes.player import Computer, Human, types_of_players
from classes.bag import Bag

QUANTITY_PLAYERS = 2  # по умолчанию игроков два
MAX_PLAYERS = 4


# может перенести в описание класса Player?
def choose_who():
    print('Выбираем тип игрока из ')
    for t in range(0, len(types_of_players)):
        print(f' {types_of_players[t]} - {t} ')
    try:
        who = int(input(f'Введите тип игрока (по умолчанию тип {types_of_players[0]}) :'))
        if who > len(types_of_players): raise ValueError
    except ValueError:
        who = 0
        print(f'Установлен тип по умолчанию {types_of_players[0]}')
    return who


class Game:

    def __init__(self):
        self.bag = Bag()
        self.is_run = True
        self.players = []

        # набираем игроков
        try:
            quantity_players = int(
                input(f'Введите количество игроков (не более {MAX_PLAYERS}, по умолчанию  {QUANTITY_PLAYERS}) :'))
            if (quantity_players < 1) or (quantity_players > MAX_PLAYERS): raise ValueError
        except ValueError:
            quantity_players = QUANTITY_PLAYERS
            print(f'Установлено количество игроков по умолчанию {QUANTITY_PLAYERS}')

        for i in range(1, quantity_players + 1):
            # присваиваем тип игрока
            self.players.append(Human(i) if choose_who() else Computer(i))
            # TODO: проверка типов

    # Вытаскиваем бочонок
    # TODO: перенести в класс Bag
    def get_barrel(self):
        print('\nКручу-верчу запутать хочу ...')
        barrel = random.choice(self.bag.barrels)
        print(f'Номер {barrel} !!!\n')
        self.bag.barrels.remove(barrel)
        self.is_run = (len(self.bag.barrels) != 0)  # последний бочонок, игра закончилась
        return barrel
