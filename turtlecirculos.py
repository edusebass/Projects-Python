from turtle import *
import colorsys
import time
bgcolor("black")
pensize(4)
tracer(50)
h = 0
for i in range(750):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.005
    up()
    goto(-8,25)
    fd(i)
    rt(90)
    fillcolor(c)
    begin_fill()
    circle(15, 320)
    end_fill()
    lt(179)
    fd(i * 2)
done(time.sleep(3))
