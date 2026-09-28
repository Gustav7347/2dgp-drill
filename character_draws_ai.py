import argparse
import math
from pathlib import Path

from pico2d import *


FRAME_DELAY = 0.01
PIXELS_PER_FRAME = 5
RECTANGLE = ((50, 550), (750, 550), (750, 50), (50, 50))
TRIANGLE = ((100, 100), (700, 100), (400, 500))


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_circle():
    for degree in range(361):
        angle = math.radians(degree)
        draw_boy(400 + 200 * math.cos(angle),
                 300 + 200 * math.sin(angle))


def move_polygon(vertices):
    for start, end in zip(vertices, vertices[1:] + vertices[:1]):
        steps = max(1, math.ceil(math.dist(start, end) / PIXELS_PER_FRAME))
        for step in range(steps + 1):
            t = step / steps
            x = start[0] + (end[0] - start[0]) * t
            y = start[1] + (end[1] - start[1]) * t
            draw_boy(x, y)


def move_rectangle():
    move_polygon(RECTANGLE)


def move_triangle():
    move_polygon(TRIANGLE)


def main(cycles=None):
    global boy
    if cycles is not None and cycles < 1:
        raise ValueError('cycles must be at least 1')
    image_path = Path(__file__).with_name('character.png')
    open_canvas(800, 600)
    try:
        boy = load_image(str(image_path))
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
    if args.cycles is not None and args.cycles < 1:
        parser.error('--cycles must be at least 1')
    try:
        main(cycles=args.cycles)
    except KeyboardInterrupt:
        pass
