from turtle import Turtle, Screen
import random

race_is_on=False

screen=Screen()
screen.setup(width=800, height=400)
screen.bgcolor('black')
user_bet = screen.numinput('Bet On A Turtle', "Select from 1,2,3,4", 4, 1)

if user_bet:
    race_is_on=True

turtle1=Turtle()
turtle1.shape('turtle')
turtle1.color('red')
turtle1.penup()
turtle1.goto(-350, 150)

turtle2=Turtle()
turtle2.shape('turtle')
turtle2.color('blue')
turtle2.penup()
turtle2.goto(-350, 50)

turtle3=Turtle()
turtle3.shape('turtle')
turtle3.color('green')
turtle3.penup()
turtle3.goto(-350, -50)

turtle4=Turtle()
turtle4.shape('turtle')
turtle4.color('yellow')
turtle4.penup()
turtle4.goto(-350,-150)

all_turtles=[turtle1, turtle2, turtle3, turtle4]

while race_is_on:

    for turtles in all_turtles:
        if turtles.xcor() > 380:
            winning_turtle_color = turtles.pencolor()
            if winning_turtle_color=='red':
                winning_turtle_number=1
            elif winning_turtle_color=='blue':
                winning_turtle_number=2
            elif winning_turtle_color=='green':
                winning_turtle_number=3
            elif winning_turtle_color=='yellow':
                winning_turtle_number=4
            race_is_on=False
        turtles.forward(random.randint(1,10))

if race_is_on==False:
    print(f"Turtle {winning_turtle_number} won the race.")
if winning_turtle_number==user_bet:
    print("You win")
else:
    print("You lose")

screen.exitonclick()