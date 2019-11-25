"""
ЛОТО
"""
from classes.game import Game

if __name__ == '__main__':

    loto = Game()
    loto.start()

    while loto.is_run:
        # вытаскиваем очередной бочонок
        barrel = loto.get_barrel()

        # что у игроков ?
        for player in loto.players:
            player.show_cards()  # показываем карточку
            player.move_on()  # делаем ход

        loto.is_run = False

    loto.finish()
