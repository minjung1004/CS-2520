#Name: Min Jung
#Due Date: November 12, 2021
#Assignment 6: Lab 2

import turtle

turtle.penup()
turtle.backward(350)
turtle.pendown()
#Triangle
numside = 3
length = 100
angle = 360/numside
turtle.fillcolor("green")
turtle.begin_fill()
for i in range(numside):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.penup()
turtle.forward(200)
turtle.pendown()
    
#Pentagon
numside = 5
length = 100
angle = 360/numside
turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(numside):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()
    
turtle.penup()
turtle.forward(300)
turtle.pendown()
    
#Octatagon
numside = 8
length = 100
angle = 360/numside
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(numside):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()