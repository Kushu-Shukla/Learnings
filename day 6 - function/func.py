import turtle

kushu = turtle.Turtle()

turtle.speed(10)

def sqaure():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)

for i in range(100):
    sqaure()
    turtle.forward(100)
    turtle.left(90)

def coffee():
    print("take milk boil it")
    print("add sugar")
    print("add coffee")

coffee()