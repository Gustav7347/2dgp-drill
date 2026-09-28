from pathlib import Path
import math

from pico2d import *


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for degree in range(361):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_boy(x, y)


def move_top():
    for x in range(50, 751, 5):
        draw_boy(x, 550)


def move_right():
    for y in range(550, 49, -5):
        draw_boy(750, y)


def move_bottom():
    for x in range(750, 49, -5):
        draw_boy(x, 50)


def move_left():
    for y in range(50, 551, 5):
        draw_boy(50, y)


def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_line(start, end):
    for step in range(101):
        t = step / 100
        x = start[0] + (end[0] - start[0]) * t
        y = start[1] + (end[1] - start[1]) * t
        draw_boy(x, y)


def move_triangle_bottom():
    move_line((100, 100), (700, 100))


def move_triangle_right():
    move_line((700, 100), (400, 500))


def move_triangle_left():
    move_line((400, 500), (100, 100))


def move_triangle():
    move_triangle_bottom()
    move_triangle_right()
    move_triangle_left()


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
