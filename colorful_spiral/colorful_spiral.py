from turtle import Turtle, Screen
from colors_list import colors_list
from random import choice

screen = Screen()
screen.bgcolor('black')

pen = Turtle()
pen.hideturtle()
pen.speed(0)

def draw_line(distance):
    pen.forward(distance/2)
    pen.backward(distance)
    pen.forward(distance/2)

length = 1440

while length!=0:
    pen.color(choice(colors_list))
    draw_line(length)
    pen.right(3)
    length = length - 8

screen.exitonclick()