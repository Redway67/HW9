# coding=utf-8
"""
Класс Player
"""
from classes.card import Card

QUANTITY_CARDS = 1  # по умолчанию карточек 1

# типы игроков
types_of_players = {0: 'Компьютер', 1: 'Человек'}


class Player:

    def __init__(self, number=1):
        self.number = number
        self.is_playing = True
        # присваиваем имя игрока
        name_player = input(f'Введите имя (по умолчанию Неизвестный #{number}) :')
        self.name = (name_player if name_player else 'Неизвестный ' + '#' +str(number))
        # TODO: проверить имя на уникальность
        # заполняем карточку игрока
        self.cards = Card()  # можно потом сделать по нескольку карт на игрока

    def show_cards(self):
        self.cards.show_card()

    def move_on(self, barrel):
        print('Хожу')


class Human(Player):

    def __init__(self, number=1):
        super().__init__(number)

    def move_on(self, barrel):
        if self.is_playing:
            print(f'Ход: {self.name} (человек)')
            self.cards.show_card()
            answer = input('Зачеркнуть цифру? (y / n)').lower()
            # исключим ошибку: русская 'н' на той же клавише , что и английская 'y'
            if (answer == 'y') or (answer == 'н'):
                if barrel in self.cards.field:
                    print(f'Есть номер {barrel}!')
                    self.cards.close_box(self.cards.field.index(barrel))
                    return 0 if self.cards.is_empty() else 1  # 0-продолжить игру, 1- карточка заполнена
                else:
                    print(f'Ошибка: зачеркнутой цифры у Вас нет! Игрок {self.name} вылетает.')
                    self.is_playing = False
                    return 2  # ошибка: нет зачеркнутой цифры
            else:
                if barrel in self.cards.field:
                    print(f'Ошибка: пропущена цифра! Игрок {self.name} вылетает.')
                    self.is_playing = False
                    return 3  # ошибка: пропущена цифра
                else:
                    print('Мимо!\n')
        else:
            print(f'{self.name} не играет')
        return 0  # продолжаем играть


class Computer(Player):

    def __init__(self, number=1):
        super().__init__(number)

    def move_on(self, barrel):
        print(f'Ход: {self.name} (компьютер)')
        self.cards.show_card()
        if barrel in self.cards.field:
            print(f'Есть номер {barrel}!')
            self.cards.close_box(self.cards.field.index(barrel))
        else:
            print('Мимо!\n')

        return 0 if self.cards.is_empty() else 1  # 0-продолжить игру, 1- карточка заполнена
