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
            result = player.move_on(barrel)  # делаем ход, 0- продолжаем
            if result == 1:
                print('Победа ! Карточка заполнена! Игра закончена')
                loto.is_run = False
                break

    loto.finish(player.name)
    del loto
