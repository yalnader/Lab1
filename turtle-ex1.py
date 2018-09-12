import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

# Create the x y planes

t.forward(100)
t.left(180)
t.forward(200)
t.right(180)
t.forward(100)
t.right(90)
t.forward(100)
t.left(180)
t.forward(200)

# Create circle_1
t.penup()
t.goto(15, 0)
#t.goto(-7.5, -15)
t.pendown()
#t.right(90)
#t.forward(7.5)
t.circle(15)

# Create circle_2
t.penup()
t.goto(30, 0)
#t.goto(-30, 15)
t.pendown()
#t.right(90)
#t.forward(15)
t.circle(30)

# Create circle_3
t.penup()
t.goto(40, 0)
#t.goto(20, 40)
t.pendown()
#t.right(90)
#t.forward(20)
t.circle(40)

# Create circle_4
t.penup()
t.goto(5, 0)
#t.goto(2.5, 5)
t.pendown()
#t.right(90)
#t.forward(2.5)
t.circle(5)

# Create X
t.penup()
t.goto(0, 0)
t.setheading(45)
t.pendown()
t.forward(100)
t.left(180)
t.forward(200)
t.penup()
t.goto(0, 0)
t.setheading(135)
t.pendown()
t.forward(100)
t.right(180)
t.forward(200)





