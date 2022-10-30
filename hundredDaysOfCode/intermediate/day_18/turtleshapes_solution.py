import turtle as t
import random

tshepiso = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# num_sides = 5 #draw pentagon

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tshepiso.forward(100)
        tshepiso.right(angle)

# loop between numbers 3 and 10. 11 is excluded
for shape_side_n in  range(3, 11):
    tshepiso.color(random.choice(colours))
    draw_shape(shape_side_n)