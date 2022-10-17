import keyboard
import os
import time


def menu_switcher(menu, position=1):

    if position < 1:
        position = 1
    if position > len(menu):
        position = len(menu)
    os.system('cls')
    print('Menu:')
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
            menu_switcher(menu, position)
        case "down":
            position += 1
            menu_switcher(menu, position)
        case "enter":
            return position
        case _:
            menu_switcher(menu, position)


# menu = ['Скачать видеофайл со звуком', 'Выбрать дорожки самостоятельнор',
#         'Настройка работы с файлами', 'Настройка ffmpeg']

# menu_switcher(menu)

