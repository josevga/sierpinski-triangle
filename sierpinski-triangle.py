# sierpinski-triangle.py
# Program to draw Sierpinski triangle using arcade module

import sys
import arcade
from random import randint

if len(sys.argv) > 1:
    num_points = int(sys.argv[1])
else:
    num_points = 50000

if num_points < 2000:
    pixels = 4
else:
    pixels = 1

# Set constants for the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

# v is a list with triangle coord.
v = [
    {'x': 10, 'y': 10},
    {'x': 300, 'y': 590},
    {'x': 590, 'y': 10}]

# Draw a triangle
arcade.draw_line(v[0]['x'], v[0]['y'], v[1]['x'], v[1]['y'], arcade.color.BLACK)
arcade.draw_line(v[1]['x'], v[1]['y'], v[2]['x'], v[2]['y'], arcade.color.BLACK)
arcade.draw_line(v[2]['x'], v[2]['y'], v[0]['x'], v[0]['y'], arcade.color.BLACK)

# Drawing random points
x, y = 300, 300
for i in range(num_points):
    i = randint(0, 2)
    x, y = x + (v[i]['x'] - x) / 2, y + (v[i]['y'] - y) / 2
    arcade.draw_point(x, y, arcade.color.BLACK, pixels)

# Finish the render and keep the window up until someone closes it.
arcade.finish_render()
arcade.run()
