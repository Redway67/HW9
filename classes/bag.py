"""
Класс Bag
"""

import random
QUANTITY_BARRELS = 90


class Bag:

    def __init__(self):
        self.barrels = list(range(1, QUANTITY_BARRELS + 1))
        random.shuffle(self.barrels)
