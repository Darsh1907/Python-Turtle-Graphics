from turtle import Turtle, Screen

screen=Screen()
pen=Turtle()

pen.color('black')
pen.shape('arrow')


def move_forwards():
    pen.forward(3)
def move_backwards():
    pen.back(3)
def turn_left():
    pen.left(3)
def turn_right():
    pen.right(3)
def clear_screen():
    pen.setx(0)
    pen.sety(0)   # Or just use pen.home()
    pen.setheading(0)
    pen.clear()


screen.listen()
screen.onkeypress(key = 'w', fun = move_forwards)
screen.onkeypress(key = 's', fun = move_backwards)
screen.onkeypress(key = 'd', fun = turn_right)
screen.onkeypress(key = 'a', fun = turn_left)
screen.onkeypress(key = 'c', fun=clear_screen)


screen.exitonclick()