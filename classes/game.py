"""
Класс Game
"""

from classes.player import Player, types_of_players

QUANTITY_PLAYERS = 2  # по умолчанию игроков два


class Game:

    def __init__(self):
        self.players = []
        self.bag = {}
        self.is_run = True
        self.quantity_players = QUANTITY_PLAYERS

    # Вытаскиваем бочонок
    def get_barrel(self):
        barrel = 0
        print('Кручу-верчу запутать хочу!!')
        return barrel

    # определяем размеры карточек, количество и полей
    def init_cards(self):
        # TODO: обработка ввода карточек
        print('КАРТОЧКИ:')
        w_card = int(input('Введите ширину карточки (по умолчанию 9):'))
        h_card = int(input('Введите высоту карточки (по умолчанию 3):'))
        f_card = int(input('Введите заполненость полей карточки (по умолчанию 5):'))
        n_card = int(input('Введите количество карточек (по умолчанию 1):'))
        dim_card = (w_card, h_card, f_card, n_card)
        return dim_card

    # набираем игроков
    def init_players(self, dim_card):
        # TODO: обработка ввода количества игроков, имени и тип игрока
        print('ИГРОКИ:')
        quantity_players = int(input('Сколько будет игроков (по умолчанию 2):'))  # TODO: умолчание константа!
        if quantity_players >= 2:
            self.quantity_players = quantity_players

        print('Выбираем игроков:')
        for i in range(1, self.quantity_players + 1):
            print(f'Игрок №{i}')

            # придумаем имя
            name_player = input(f'Введите имя (по умолчанию Неизвестный № {i}) :')
            if name_player:
                name_player = 'Неизвестный № ' + str(i)

            # выбирем тип
            type_player = int(input(f'Введите тип игрока (по умолчанию тип {types_of_players[1]}) :'))
            new_player = Player(name_player, type_player, dim_card)

            self.players.append(new_player)

    # Старт игры
    def start(self):
        print('Рассказываем правила ...')

        print('Определяем размеры карточек и полей')
        dim_card = self.init_cards()  # определяем размеры, количество карточек и полей

        print('Набирем игроков')
        self.init_players(dim_card)  # набираем игроков

        print('Поехали!')

    # Финиш игры
    def finish(self):
        print(f'Победитель')
