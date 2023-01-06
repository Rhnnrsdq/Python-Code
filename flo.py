from turtle import *
from colorsys import *


bgcolor('light blue')
shape('turtle')
speed(0)
hue = 0.9

for j in range(182):
    col = hsv_to_rgb(hue, 1, 1)
    hue += 0.005
    color(col, col)
    begin_fill()
    circle(190 - j, 100)
    left(90)
    circle(190 - j, 100)
    end_fill()

done()
