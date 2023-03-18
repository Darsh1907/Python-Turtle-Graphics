from turtle import Turtle, Screen

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

t = Turtle()
t.speed(1000000)

screen = Screen()
screen.bgcolor('black')

for x in range(10000):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

screen.exitonclick()
