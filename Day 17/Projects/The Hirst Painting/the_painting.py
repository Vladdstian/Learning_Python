# make the turtle create a Hirst painting
# I did the project and manually created the dots until I saw at the end that there is a dot method :|

import random
import colorgram
import turtle as t

t.colormode(255)


def draw_painting(dot_radius, lateral_len, turtle_obj, color_lst):
    y_pos = -350
    rows = lateral_len
    while rows != 0:
        columns = lateral_len
        while columns != 0:
            turtle_obj.pendown()
            color = random.choice(color_lst)
            turtle_obj.color(color)
            turtle_obj.begin_fill()
            turtle_obj.circle(dot_radius)
            turtle_obj.end_fill()
            turtle_obj.penup()
            turtle_obj.forward(50 + 2 * dot_radius)
            columns -= 1
        turtle_obj.setposition(x=-350, y=-350)
        y_pos += 50 + 2 * dot_radius
        turtle_obj.sety(y_pos)
        rows -= 1


color_list = []
num_of_colors = 30
colors = colorgram.extract("swiss.jpg", num_of_colors)
for _ in range(num_of_colors):
    rgb = colors[_].rgb
    color_sum = rgb.r + rgb.g + rgb.b
    if color_sum < 700:
        color_tuple = (rgb.r, rgb.g, rgb.b)
        color_list.append(color_tuple)
    else:
        continue

bob = t.Turtle()
bob.speed("fastest")
bob.penup()
bob.setposition(x=-350, y=-350)
draw_painting(10, 10, bob, color_list)

screen = t.Screen()
screen.exitonclick()
