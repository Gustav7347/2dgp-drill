from pathlib import Path
import math

from pico2d import *


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for degree in range(91):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_boy(x, y)


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
