#Turtle documentation
# https://docs.python.org/3/library/turtle.html#turtle.shape

import turtle

#Screen is a complex data type - 
# meaning that it has attributes and behaviors
screen = turtle.Screen() #this is the instantiation call for the object screen
screen.title("Turtle Example in Python")

# Create a turtle object
#Turtle is a complex data type 
poly = turtle.Turtle() #This is the instantiation of an object
lion = turtle.Turtle() #Instantiation of a new turtle object
poly.color("red")
poly.shape("turtle")

#poly.circle(50)
# Move the turtle forward by 100 units
# --forward100 is a non-fruitful function because it does
#   not return a value, it simply performs an action,
#   which is to move the turtle forward 100

# Turn the turtle to the right by 90 degrees
# --right90 is a non-fruitful function because it does
#   not return a value, it simply performs an action,
#   which is to turn the turtle 90 degrees to the right

def square(aTurtle):
    for i in range(4):
        aTurtle.forward(100)
        aTurtle.right(90)

def pentagon():
    for i in range(5):
        poly.forward(100)
        poly.right(72)

def regularPolygon(sides):
    interiorAngle = 180 - ((sides - 2) * 180) / sides
    for i in range(sides):
        poly.forward(100)
        poly.right(interiorAngle)

def make_circle():
    poly.circle(50)

# subjects is a list which is a complex data type
# subjects contains a length of 5.
# for loop is for finite loops
# ITERATION - looping through code over and over again
def iterationTesting():

    subjects = ["English", "Math", "Science", "Health", "Economics"]
    for subject in subjects:
        print("My favorite subject is: ", subject)

    counter = 0
    while(counter <= len(subjects)):
        print("Counter: ", counter)
        # increment the counter
        counter = counter + 1

    #do {
    # this code will run at least once
    # } while a condition a met

def rainbow():
    colors = ["red","orange","yellow","green","blue","indigo","violet"]
    for color in colors:
        poly.color(color)
        poly.forward(10)
        poly.circle(20)
        poly.forward(10)

def backForth():
    poly.forward(-300)
    poly.speed(10)
    colors = ["red","orange","yellow","green","blue","indigo","violet"]
    for color in colors:
        poly.color(color)
        poly.pensize(3)
        poly.forward(100)
        poly.forward(-50)

def funActivityWithTurtles():
    size = 20
    #penup and pendown function

    #stamp function
    for i in range(30):
        poly.stamp()
        poly.penup()
        size = size + 3
        poly.forward(size)
        poly.pendown()
        poly.right(24)

def print1000times(message):
    for i in range(1000):
        print(message)

def printMonths():
    months = ["January", "February", "March", "April", "May"]
    for month in months:
        print("Welcome to the month of ", month)

def turnLeft3645(aTurtle):
    aTurtle.left(3645)

#TEST SUITE

#funActivityWithTurtles()
#screen is a Screen object and it has behaviors
# like onkey, onkeypress
screen.onkey(square, "Up")
screen.onkey(pentagon, "Right")
screen.onkey(make_circle, "Left")
#regularPolygon(int(input("Number of sides: ")))
#rainbow()
#backForth()

print1000times("I love Python")
printMonths()
turnLeft3645(poly)
#square(poly)
#square(lion)

screen.listen()
screen.mainloop()

# Keep the window open until clicked
turtle.done()

