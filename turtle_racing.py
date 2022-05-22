from turtle import Turtle, Screen
from random import choice, randint

y_cor = [-100, -50, 0, 50, 100]
colours = ['red', 'blue', 'green', 'black', 'yellow']
all_turtles = []
game_on = False


screen = Screen()
screen.setup(500, 400)
user_choice = screen.textinput('Place your bet', 'Enter the colour of the turtle you want to bet. ')

for i in range(0, 5):
    turtle1 = Turtle('turtle')
    turtle1.color(colours[i])
    turtle1.penup()
    turtle1.goto(-240, y_cor[i])
    all_turtles.append(turtle1)

if user_choice:
    game_on = True

while game_on:
    for i in range(0, 5):
        all_turtles[i].pendown()
        if all_turtles[i].xcor() > 230:
            game_on = False
            colour = all_turtles[i].pencolor()
            if user_choice.lower() == all_turtles[i].pencolor():
                print(f'You win, {all_turtles[i].pencolor()} has won the game. ')

            else:
                print(f'You loose, {all_turtles[i].pencolor()} has won the game. ')
        else:
            speed = randint(0, 10)
            all_turtles[i].forward(speed)

screen.exitonclick()
