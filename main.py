import turtle

import colorgram
from turtle import Turtle, Screen
import random

turtle.colormode(255)
colors = colorgram.extract('image.jpeg',30)
squirtle = Turtle()
squirtle.speed("fastest")
squirtle.penup()
squirtle.hideturtle()
rows = 10
columns = 10
dot_size = 20
spacing = 50

start_x = -columns * spacing // 2
start_y = -rows * spacing // 2

for row in range(rows):
    for col in range(columns):
        color = random.choice(colors).rgb
        r = color.r
        g = color.g
        b = color.b
        squirtle.goto(start_x + col * spacing, start_y + row * spacing)
        squirtle.dot(dot_size, (r, g, b))


myScreen = Screen()
myScreen.exitonclick()