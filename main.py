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
    print('Поехали!')

    loto = Game()
    while loto.is_run:
        # вытаскиваем очередной бочонок
        barrel = loto.get_barrel()
        # что у игроков ?
        for player in loto.players:
            result = player.move_on(barrel)  # 0- продолжаем
            if result == 1:
                print('\nПобеда !!! Карточка заполнена. Игра закончена')
                loto.is_run = False
                break

    print(f'Победитель {player.name}')
    del loto
