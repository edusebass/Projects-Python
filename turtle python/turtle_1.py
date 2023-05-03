import turtle
import random

t = turtle.Turtle()
turtle.bgcolor("black")
colors = ["red", "orange", "yellow", "green", "green", "blue", "purple"] 

while True:
    t.penup()
    x = random.randint(-200,200)
    y = random.randint(-200, 200)
    t.goto(x , y)
    size = random.randint(10, 100)
    t.pendown()
    t.color(random.choice(colors))
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()
    t.home()
    t.right(random.randint(0, 360))