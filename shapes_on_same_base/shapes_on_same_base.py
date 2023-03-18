from turtle import Turtle, Screen
from random import choice

a=Turtle()

a.shape='arrow'
a.speed(8)

from colors_list import colors_list

n=4
while n<11:
    a.color(choice(colors_list))
    angle=(360/n)
    for _ in range(1,n+1):
        a.forward(100)
        a.left(angle)
    n=n+1

screen=Screen()
screen.exitonclick()