from turtle import Turtle, Screen

dash = Turtle()

for _ in range(10):
    dash.forward(10)
    dash.penup()
    dash.forward(10)
    dash.pendown()
    # dash.left(90)


screen = Screen()
screen.exitonclick()