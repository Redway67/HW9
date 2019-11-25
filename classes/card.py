"""
Класс Card
"""
# размеры карточек, заполненость, количество по умолчанию
CARD_WIDTH = 9
CARD_HEIGHT = 3
CARD_FILLED = 5
CARD_QUANTITY = 1


class Card:

    def __init__(self):
        self.width = CARD_WIDTH
        self.heght = CARD_HEIGHT
        self.filled = CARD_FILLED
        self.quantity = CARD_QUANTITY
