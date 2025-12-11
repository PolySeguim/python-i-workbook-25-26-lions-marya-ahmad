import turtle

#screen is an object of the Screen class
screen = turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("lightgreen")

#marya is an object of the Turtle class
marya = turtle.Turtle()
marya.shape("turtle")
marya.color("blue")

"""
def draw_clock():
   for i in range(12):
    marya.speed(0)
    marya.stamp()
    marya.penup()
    marya.forward(150)
    marya.pendown()
    marya.stamp()
    marya.penup()
    marya.backward(150)
    marya.right(30)
    marya.pendown()
draw_clock()
"""
"""
def draw_spiral():
    marya.speed(0)
    length = 2
    distance = 5
    for i in range(150):
        distance = distance + length
        marya.forward(distance) 
        marya.right(90)
draw_spiral()
"""
def draw_spiralwithtwist():
    marya.speed(0)
    length = 2
    distance = 5
    for i in range(120):
        distance = distance + length
        marya.forward(distance) 
        marya.right(45)
draw_spiralwithtwist()

screen.listen()
screen.mainloop()


