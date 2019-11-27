"""
Класс Card
"""
import random
from classes.bag import QUANTITY_BARRELS

# размеры карточек, заполненость, количество по умолчанию
CARD_WIDTH = 9
CARD_HEIGHT = 3
CARD_FILLED = 5
EMPTY_BOX = 0


class Card:

    def __init__(self, number=1):
        self.number = number

        # заполняем карточку
        self.field = []
        population = list(range(1, QUANTITY_BARRELS + 1))  # все бочонки от 1 и до максиума
        position = list(range(0, CARD_WIDTH))  # позиции от 0 до ширины строки карточки
        for i in range(0, CARD_HEIGHT):
            row_population = sorted(random.sample(population, CARD_FILLED))
            filled_position = sorted(random.sample(position, CARD_FILLED))
            row = [row_population[filled_position.index(i)] if i in filled_position else EMPTY_BOX for i in
                   range(0, CARD_WIDTH)] # заполняем. если пусто , то 0
            self.field.append(row)

    def show_card(self):
        for i in range(0, CARD_HEIGHT):
            print(self.field[i])
