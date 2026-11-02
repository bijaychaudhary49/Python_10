
import turtle

# Create the first turtle
t = turtle.Turtle()

# Move the turtle forward and clear the drawing
t.forward(100)
t.clear()
t.backward(100)
t.clear()

# Change the turtle's direction
t.right(90)
t.left(90)

# Move the turtle to a specific position
t.goto(100, 100)

# Change the turtle's shape
t.shape("turtle")
t.shape("circle")
t.shape("square")
t.shape("triangle")
t.shape("arrow")

# Draw lines and clear the screen
t.clear()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

t.clear()

# Draw a square using a loop
for i in range(4):
    t.forward(100)
    t.left(90)

# Draw a triangle using a loop
for i in range(3):
    t.forward(100)
    t.left(120)

# Create two more turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()

# Move the second turtle to a new position
t2.goto(-200, -200)
t2.clear()
t.clear()

# Draw a square
for i in range(4):
    t.forward(100)
    t.left(90)

# Draw a rectangle
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t.forward(50)
    t1.left(90)

# Clear the first turtle's drawing
t1.clear()

# Draw a rectangle using the first turtle
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(50)
    t1.left(90)

# Draw a triangle using the second turtle
for i in range(3):
    t2.forward(200)
    t2.left(120)

# Clear all drawings
t1.clear()
t2.clear()
t.clear()

# Draw circles of different sizes
t.circle(10)
t1.circle(100)
t2.circle(200)

# Clear the drawings
t.clear()
t1.clear()
t2.clear()

# Change the pen color and draw a circle
t.pencolor("red")
t.color("blue")
t.circle(100)

# Change the second turtle's color
t2.color("green")
t2.fillcolor("red")

# Draw a filled circle
t2.begin_fill()
t2.circle(150)
t2.end_fill()

# Move the first turtle forward
t1.forward(100)

# Lift the pen so it does not draw
t1.penup()
t1.forward(1000)
t1.backward(1000)
t1.forward(50)

# Put the pen down to start drawing again
t1.pendown()
t1.forward(100)

# Change the background color
turtle.bgcolor("green")

# Hide and show the turtle
t.hideturtle()
t.showturtle()

# Clear the second turtle's drawing
t2.clear()

# Draw a pentagon using a loop
for i in range(5):
    t2.forward(100)
    t2.left(72)

# Change the turtle's color and pen thickness
t2.color("red")
t2.pensize(2)

# Draw another pentagon
for i in range(5):
    t2.forward(100)
    t2.left(72)

# Change pen thickness and colors
t2.pensize(10)
t2.color("yellow")
t2.fillcolor("pink")

# Draw a filled pentagon
t2.begin_fill()

for i in range(5):
    t2.forward(100)
    t2.left(72)

# Finish filling the pentagon
t2.end_fill()

# Keep the turtle graphics window open
turtle.done()
