"""
Класс Bag
"""
from classes.barrel import Barrel

QUANTITY_BARRELS = 90


class Bag:

    def __init__(self, quantity_barrels=QUANTITY_BARRELS):
        self.barrels = [Barrel(i) for i in range(1, quantity_barrels+1)]
