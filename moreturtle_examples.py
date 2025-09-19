import turtle

#screen is a complex data type -
# meaning that it has attributes and behaviora 
# Create a turtle object
screen = turtle.Screen() #this is the instantiation call for the object screen
screen.title("Turtle Example in Python")

#create a turtle object
#turtle is a complex data type
marya = turtle.Turtle() #this is the instantiation of the an object
marya.color("red")
marya.shape("turtle")

# Move the turtle forward by 100 units
# --forward100 is a non-fruitful function bexcause 
# it does not return a value, it simpl preforms an action
# which is to move the turtle forward
def forward100():
    marya.forward(100)

# Turn the turtle to the right by 90 degrees
# --right90 is a non-fruitful function because it does
# not return a value, it simply performs an action
# which is to turn the turtle right 90 degrees
def right90():   
    marya.right(90)


def rainbow():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        marya.color(color)
        marya.forward(10)
        marya.circle(20)
        marya.forward(10)


#screen is a screen object and it has behaviors
# like onkey, onkeypress
screen.onkey(forward100, "Up") 
screen.onkey(right90, "Right")  


screen.listen() 
screen.mainloop() 
rainbow()
# Keep the window open until clicked
turtle.done()