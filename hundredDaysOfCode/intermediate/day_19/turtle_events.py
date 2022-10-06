from turtle import Turtle, Screen

sfiso = Turtle()
screen = Screen()

def move_forwards():
    sfiso.forward(10)

# listen for events
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()