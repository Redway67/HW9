"""
Класс Game
"""
import random
from classes.player import Computer, Human, types_of_players
from classes.bag import Bag

QUANTITY_PLAYERS = 2  # по умолчанию игроков два


def choose_who():
    print('Выбираем тип игрока из ')
    for t in range(0, len(types_of_players)):
        print(f' {types_of_players[t]} - {t} ')
    try:
        who = int(input(f'Введите тип игрока (по умолчанию тип {types_of_players[0]}) :'))
        if who > len(types_of_players): raise ValueError
    except ValueError:
        who = 0
        print(f'Ошибка! Установлен тип по умолчанию {types_of_players[0]}')
    return who


class Game:

    def __init__(self):
        self.bag = Bag()
        self.is_run = True
        self.players = []
        # набираем игроков
        for i in range(1, QUANTITY_PLAYERS + 1):
            # присваиваем тип игрока
            self.players.append(Human(i) if choose_who() else Computer(i))
            # TODO: проверка типов

    # Вытаскиваем бочонок
    def get_barrel(self):
        print('Кручу-верчу запутать хочу ...')
        barrel = random.choice(self.bag.barrels)
        print(f'Номер {barrel} !!!')
        self.bag.barrels.remove(barrel)
        self.is_run = (len(self.bag.barrels) != 0)  # последний бочонок, игра закончилась
        print('')
        return barrel

    # Старт игры
    def start(self):
        print('Рассказываем правила ...')
        print('Поехали!')

    # Финиш игры
    def finish(self, winner):
        print(f'Победитель {winner}')
