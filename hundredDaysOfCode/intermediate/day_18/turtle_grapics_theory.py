from turtle import Turtle, Screen

import heroes

thulani_the_turtile = Turtle()
thulani_the_turtile.shape("turtle")

print(heroes.gen())
screen = Screen()
screen.exitonclick()