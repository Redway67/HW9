"""
Класс Game
"""

from classes.player import Computer, Human, types_of_players
from classes.bag import Bag

QUANTITY_PLAYERS = 2  # по умолчанию игроков два
MAX_PLAYERS = 4


class Game:

    def __init__(self, running_players=QUANTITY_PLAYERS):
        self.bag = Bag()
        self.is_running = True
        self.players = []
        self.running_players = running_players
        self.lap = 1

    def __str__(self):
        return f'Игроков {len(self.players)} , Раунд {self.lap}'

    def __eq__(self, other):
        # ровно количество играющих в текущем раунде.
        return self.running_players == other.running_players

    # Вытаскиваем и показываем бочонок
    def pull_out_barrel(self):
        print(f'РАУНД № {self.lap}')
        print('Кручу-верчу запутать хочу ...')
        self.bag.shake_bag()
        barrel = self.bag.get_barrel()
        print(f'Номер {barrel} !!!')
        self.bag.throw_out_barrel(barrel)
        self.is_running = self.bag.is_not_empty()  # последний бочонок, игра закончилась
        print(f'В мешке осталось {self.bag.is_not_empty()} бочонков \n')
        self.lap += 1
        return barrel


# if __name__ == '__main__':
#     game1 = Game()
#     game2 = Game()
#     print(game1)
#     print(game2)
#     print(game1 == game2)  # в начале игры
