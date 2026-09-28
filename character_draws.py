from pico2d import *


def move_circle():
    print('circle')


def move_rectangle():
    print('rectangle')


def move_triangle():
    print('triangle')


def main(cycles=1):
    open_canvas(800, 600)
    for _ in range(cycles):
        move_circle()
        move_rectangle()
        move_triangle()
    close_canvas()


if __name__ == '__main__':
    main()
