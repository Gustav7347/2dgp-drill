from pathlib import Path

from pico2d import *


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    draw_boy(400, 300)


def move_rectangle():
    print('rectangle')


def move_triangle():
    print('triangle')


def main(cycles=1):
    global boy
    open_canvas(800, 600)
    boy = load_image(str(Path(__file__).with_name('character.png')))
    for _ in range(cycles):
        move_circle()
        move_rectangle()
        move_triangle()
    close_canvas()


if __name__ == '__main__':
    main()
