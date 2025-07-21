# Timothy Jones
# 7/16/2025
# P4LAB1
# Draw a square and triangle using turtle graphics

#begin
import turtle

# Set up turtle
t = turtle.Turtle()
t.pensize(3)
t.color("blue")

# Draw square using a for loop
for i in range(4):
    t.forward(100)
    t.left(90)

# Move turtle to a new position for the triangle
t.penup()
t.goto(150, 0)
t.pendown()
t.color("red")

# Draw triangle using a while loop
i = 0
while i < 3:
    t.forward(100)
    t.left(120)
    i += 1

# Keep the window open
turtle.done()

#end
