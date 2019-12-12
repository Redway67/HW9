"""
Класс Player
"""
from classes.card import Card

QUANTITY_CARDS = 1  # по умолчанию карточек 1

# типы игроков
types_of_players = {0: 'Компьютер', 1: 'Человек'}


class Player:

    def __init__(self, name='', number=1, who=0, ):
        self.number = number
        self.is_playing = True
        self.who = who
        # присваиваем имя игрока
        self.name = (name if name else 'Неизвестный ' + '#' + str(number))
        # заполняем карточку игрока
        self.cards = Card()  # можно потом сделать по нескольку карт на игрока

    def show_cards(self):
        print(self.cards)  # потом будем печатать много карточек

    def move_on(self, barrel):
        return 0  # переопределим метод в наследующих классах

    def __str__(self):
        return f' Игрок {self.name} '

    def __eq__(self, other):
        # равны, если их типы равны
        return self.who == other.who


class Human(Player):

    def __init__(self, name, number=1):
        super().__init__(name, number, 1)

    def move_on(self, barrel):
        if self.is_playing:
            print(f'\nХод: {self.name} (человек)')
            print(self.cards)
            answer = input('Зачеркнуть цифру? (y / n)').lower()
            # исключим ошибку: русская 'н' на той же клавише , что и английская 'y'
            if (answer == 'y') or (answer == 'н'):
                if barrel in self.cards.field:
                    print(f'Есть номер {barrel}!\n')
                    self.cards.close_box(self.cards.field.index(barrel))
                    return 0 if self.cards.is_empty() else 1  # 0-продолжить игру, 1- карточка заполнена
                else:
                    print(f'Ошибка: зачеркнутой цифры у Вас нет! ')
                    self.is_playing = False
                    return -2  # ошибка : нет зачеркнутой цифры
            else:
                if barrel in self.cards.field:
                    print(f'Ошибка: пропущена цифра! ')
                    self.is_playing = False
                    return -3  # ошибка: пропущена цифра
                else:
                    print('Мимо!\n')
        else:
            print(f'{self.name} выбыл из игры')
        return 0  # продолжаем играть


class Computer(Player):

    def __init__(self, name, number=1):
        super().__init__(name, number, 0)

    def move_on(self, barrel):
        print(f'\nХод: {self.name} ({types_of_players[self.who]})')
        print(self.cards)
        if barrel in self.cards.field:
            print(f'Есть номер {barrel}!\n')
            self.cards.close_box(self.cards.field.index(barrel))
        else:
            print('Мимо!\n')
        return 0 if self.cards.is_empty() else 1  # 0-продолжить игру, 1- карточка заполнена


# if __name__ == '__main__':
#     player1 = Human(1)
#     print(player1)
#     player2 = Computer(2)
#     print(player2)
#     print(player1 == player2)
