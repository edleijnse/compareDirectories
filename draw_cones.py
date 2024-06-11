from vpython import *

scene = canvas()
scene.width = 800
scene.height = 600

# Define all permutations of RGB color vectors
colors = [vector(1, 0, 0), vector(0, 1, 0), vector(0, 0, 1),
          vector(1, 0, 1), vector(0, 1, 1), vector(1, 1, 0), vector(0, 0, 0),  vector(1, 1, 1)]
color_index = 0
# Creating a cone. Color values in VPython are fractions of the values in the range 0 to 1.
my_cone = cone(pos=vector(0, 0, 0), radius=1, axis=vector(0, 1, 0), color=colors[color_index])

# Creating arrows
left_arrow = arrow(pos=vector(-2, -2, 0), axis=vector(-1, 0, 0), shaftwidth=0.2)
right_arrow = arrow(pos=vector(2, -2, 0), axis=vector(1, 0, 0), shaftwidth=0.2)


def move_cone(evt):
    global color_index
    clicked_object = scene.mouse.pick
    if clicked_object == left_arrow or clicked_object == right_arrow:
        color_index = (color_index + 1) % len(colors)
        my_cone.color = colors[color_index]


scene.bind('click', move_cone)

while True:
    rate(100)
