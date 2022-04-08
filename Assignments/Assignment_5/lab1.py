#Name: Min Jung
#Due Date: November 12, 2021
#Assignment 6: Lab 1

import turtle

turtle.bgcolor("dark blue")


turtle.penup()
turtle.setx(0)
turtle.sety(0)
turtle.pendown()

#Christmas Tree
numside = 3
length = 100
angle = 360/numside
turtle.pencolor("green")
turtle.fillcolor("green")
turtle.begin_fill()
for i in range(numside):
    turtle.forward(length)
    turtle.left(angle)
turtle.end_fill()

turtle.penup()
turtle.setx(-25)
turtle.sety(-70)
turtle.pendown()

numside = 3
length = 150
angle = 360/numside
turtle.pencolor("green")
turtle.fillcolor("green")
turtle.begin_fill()
for i in range(numside):
    turtle.forward(length)
    turtle.left(angle) 
turtle.end_fill()

turtle.penup()
turtle.setx(-50)
turtle.sety(-150)
turtle.pendown()

numside = 3
length = 200
angle = 360/numside
turtle.pencolor("green")
turtle.fillcolor("green")
turtle.begin_fill()
for i in range(numside):
    turtle.forward(length)
    turtle.left(angle) 
turtle.end_fill()

turtle.penup()
turtle.setx(25)
turtle.sety(-150)
turtle.pendown()

numside = 4
length = 50
angle = 360/numside
turtle.pencolor("brown")
turtle.fillcolor("brown")
turtle.begin_fill()
for i in range(numside):
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.penup()
turtle.setx(-270)
turtle.sety(200)
turtle.pendown()

#Crescent Moon
turtle.pencolor("dark blue")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.penup()
turtle.forward(25)
turtle.pendown()
turtle.fillcolor("dark blue")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.forward(25)
turtle.pendown()

#Stars --Made Big Dipper
turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()
    
turtle.penup()
turtle.setx(-200)
turtle.sety(250)
turtle.pendown()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.setx(-150)
turtle.sety(150)
turtle.pendown()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.setx(-125)
turtle.sety(200)
turtle.pendown()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(10)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.setx(-100)
turtle.sety(225)
turtle.pendown()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(10)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.right(20)
turtle.forward(100)
turtle.pendown()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(10)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.right(35)
turtle.forward(100)
turtle.pendown()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(10)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.right(300)
turtle.forward(100)
turtle.pendown()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(10)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.right(290)
turtle.forward(100)
turtle.pendown()

turtle.pencolor("white")
turtle.fillcolor("white")
turtle.begin_fill()
for i in range(5):
    turtle.forward(10)
    turtle.right(144)
turtle.end_fill()

