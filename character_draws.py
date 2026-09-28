from pathlib import Path
import math
import argparse

from pico2d import *


TRIANGLE_A = (100, 100)
TRIANGLE_B = (700, 100)
TRIANGLE_C = (400, 500)
CIRCLE_CENTER = (400, 300)
CIRCLE_RADIUS = 200
FRAME_DELAY = 0.01


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_circle():
    for degree in range(361):
        theta = math.radians(degree)
        x = CIRCLE_CENTER[0] + CIRCLE_RADIUS * math.cos(theta)
        y = CIRCLE_CENTER[1] + CIRCLE_RADIUS * math.sin(theta)
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
    steps = max(1, math.ceil(math.dist(start, end) / 5))
    for step in range(steps + 1):
        t = step / steps
        x = start[0] + (end[0] - start[0]) * t
        y = start[1] + (end[1] - start[1]) * t
        draw_boy(x, y)


def move_triangle_bottom():
    move_line(TRIANGLE_A, TRIANGLE_B)


def move_triangle_right():
    move_line(TRIANGLE_B, TRIANGLE_C)


def move_triangle_left():
    move_line(TRIANGLE_C, TRIANGLE_A)


def move_triangle():
    move_triangle_bottom()
    move_triangle_right()
    move_triangle_left()


def main(cycles=None):
    global boy
    open_canvas(800, 600)
    try:
        boy = load_image(str(Path(__file__).with_name('character.png')))
        completed = 0
        while cycles is None or completed < cycles:
            move_circle()
            move_rectangle()
            move_triangle()
            completed += 1
    finally:
        close_canvas()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Circle, rectangle, triangle motion')
    parser.add_argument('--cycles', type=int, default=None,
                        help='Run a fixed number of cycles instead of looping forever')
    args = parser.parse_args()
    main(cycles=args.cycles)
