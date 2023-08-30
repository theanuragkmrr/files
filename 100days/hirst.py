# import colorgram
# rgb_colors = []
# colors = colorgram.extract('imagee.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle

t = turtle.Turtle()
turtle.colormode(255)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68),
     (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
     (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9),
     (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202),
     (52, 234, 243), (3, 67, 40)]

t.penup()
num_dots=101
t.ht()
t.setheading(225)
t.forward(330)
t.setheading(0)
for dots in range(1, num_dots):
    t.dot(20, random.choice(color_list))
    t.forward(50)
    if dots%10==0:
        t.lt(90)
        t.fd(50)
        t.lt(90)
        t.fd(500)
        t.setheading(0)


screen=turtle.Screen()
screen.exitonclick()