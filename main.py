"""
ЛОТО
"""
from classes.game import Game

RULE_FILE = 'rule.txt'

if __name__ == '__main__':

    print('********************* ЛОТО ********************')
    print('Рассказываем правила ...')
    with open(RULE_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
    input('\n Для продолжения нажмите <ENTER>')
    loto = Game()
    print('\nПоехали!\n')
    while loto.is_run:
        # вытаскиваем очередной бочонок
        barrel = loto.show_barrel()
        # что у игроков ?
        for player in loto.players:
            result = player.move_on(barrel)  # 0- продолжаем
            if result == 1:
                print('\nПобеда !!! Карточка заполнена. Игра закончена')
                loto.is_run = False
                break
            elif result < 0:
                print(f'Игрок {player.name} выбыл из игры')
                loto.running_players -= 1
                if loto.running_players == 0:  # остались ли игроки?
                    result = -100  # никого не осталось
                    loto.is_run = False
                    break
    winner = (player.name if result != -100 else 'не определён')
    print(f'\nПобедитель {winner}  ({loto.lap - 1} раунд)')
