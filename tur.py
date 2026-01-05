import turtle
# turtle.right(60)
# turtle.forward(50)
# turtle.right(60)
# turtle.forward(50)
# turtle.right(60)
# turtle.forward(50)
# turtle.right(60)
# turtle.forward(50)
# turtle.right(60)
# turtle.forward(50)
# turtle.right(60)
# turtle.forward(50)
# turtle.done()
# turtle.right(120)
# turtle.forward(90)
# turtle.right(120)
# turtle.forward(90)
# turtle.right(120)
# turtle.forward(90)
# turtle.penup()
# turtle.left(150)
# turtle.forward(50)
# turtle.pendown()

# turtle.left(90)
# turtle.forward(90)
# turtle.left(120)
# turtle.forward(90)
# turtle.left(120)
# turtle.forward(90)
# turtle.done()

s=0
turtle.goto(80,10)
for i in range(30):
    turtle.bgcolor("yellow")
   
    turtle.left(90)
    turtle.forward(s)
    print("new position",turtle.position())
    
    s += 10
    if s==0:
        break

turtle.done()
