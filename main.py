"""
ЛОТО
"""
from classes.game import Game

if __name__ == '__main__':

    loto = Game()
    for p in loto.players:
        print(p.name)
        print(p.who)
    loto.start()

    while loto.is_run:
        # вытаскиваем очередной бочонок
        barrel = loto.get_barrel()

        # что у игроков ?
        for player in loto.players:
            print('Карточка')  # показываем карточку
            player.move_on()  # делаем ход

        loto.is_run = False

    loto.finish()
    del loto
