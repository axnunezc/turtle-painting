import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190)]

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
dots = 100

for dot_count in range(1, dots + 1):
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    
    if dot_count % 10 == 0 and dot_count < dots:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()