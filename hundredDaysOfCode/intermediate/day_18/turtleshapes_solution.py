import turtle as t

tshepiso = t.Turtle()

num_sides = 5 #draw pentagon

for _ in range(num_sides):
    angle = 360 / num_sides
    tshepiso.forward(100)
    tshepiso.right(angle)
