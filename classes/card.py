"""
Класс Card
"""
import random

from classes.bag import QUANTITY_BARRELS

# размеры карточек, заполненость, количество по умолчанию
CARD_WIDTH = 9
CARD_HEIGHT = 3
CARD_FILLED = 5


class Card:

    def __init__(self, number=1):
        self.number = number

        # заполняем карточку
        self.field = []
        population = list(range(1,QUANTITY_BARRELS+1 ))
        for i in range(0, CARD_HEIGHT):
            for j in range(0, CARD_WIDTH):
                row_sample=random.sample(population, CARD_FILLED)
                




