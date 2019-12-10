"""
Класс Bag
"""

import random

QUANTITY_BARRELS = 90


class Bag:

    def __init__(self):
        self.barrels = list(range(1, QUANTITY_BARRELS + 1))

    def shake_bag(self):
        random.shuffle(self.barrels)

    def throw_out_barrel(self, barrel):
        self.barrels.remove(barrel)

    def get_barrel(self):
        return random.choice(self.barrels)

    def is_not_empty(self):
        return len(self.barrels)

    def __str__(self):
        return f' В мешке {len(self.barrels)} шт. бочонков'


if __name__ == '__main__':

    bag = Bag()
    print(bag)
    print('Выкинем один бочонок с номером 13')
    bag.throw_out_barrel(13)
    print(bag)
