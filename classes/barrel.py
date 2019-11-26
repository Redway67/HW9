"""
Класс Barrel
"""


class Barrel:

    def __init__(self, num_barrel=0):
        self.sign = str(num_barrel)



# определяем размеры карточек, количество и полей
    # @property
    # def init_cards(self):
    #     # TODO: обработка ввода карточек
    #     print('КАРТОЧКИ:')
    #     try:
    #         w_card = int(input('Введите ширину карточки (по умолчанию 9):'))
    #     except ValueError:
    #         w_card = CARD_WIDTH
    #
    #     try:
    #         h_card = int(input('Введите высоту карточки (по умолчанию 3):'))
    #     except ValueError:
    #         h_card = CARD_HEIGHT
    #
    #     try:
    #         f_card = int(input('Введите заполненость полей карточки (по умолчанию 5):'))
    #     except ValueError:
    #         f_card = CARD_FILLED
    #
    #     try:
    #         n_card = int(input('Введите количество карточек (по умолчанию 1):'))
    #     except ValueError:
    #         n_card = CARD_QUANTITY
    #
    #     print(f'У игроков будет {n_card} карточек, размером {w_card} на {h_card}, с {f_card} заполнеными полями')
    #     dim_card = (w_card, h_card, f_card, n_card)
    #    return dim_card