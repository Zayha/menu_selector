import keyboard
import os
import time
import platform


def menu_switcher(menu, position=1, name='Menu:'):
    '''
    Формирует меню без вложений, управление стрелками вверх, вниз, выбор - стрелка вправо.

    :param menu: список пунктов меню
    :param position: С какого номера будет происходить отсчет пунктов меню
    :param name: Название меню
    :return: индекс позиции в списке menu со сдвигом position
    '''
    if platform.system() == 'Windows':
        cl = 'cls'
        # В PowerShell
    else:
        cl = 'clear'
    if position < 1:
        position = 1
    if position > len(menu):
        position = len(menu)
    os.system(cl)
    print(name)
    for i, val in enumerate(menu, start=1):
        if i == position:
            suffix = '<--'
        else:
            suffix = '   '
        print(f'[{i}]{suffix} - {val}')

    event = keyboard.read_event()
    time.sleep(0.15)
    match event.name:
        case "up":
            position -= 1
            menu_switcher(menu, position, name)
        case "down":
            position += 1
            menu_switcher(menu, position, name)
        case "right":
            # -> вместо Enter
            os.system(cl)
            return position
        case _:
            menu_switcher(menu, position, name)
