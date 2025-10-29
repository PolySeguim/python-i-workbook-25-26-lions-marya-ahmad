#Question #1 - Testing Truth Table 
def truth1(a, b, c):
    if (a and (b or c)):
        return True 
    return False
#1:
print(truth1(False, False, False)) #the answer is false
#2:
print(truth1(False, False, True)) #the answer is false
#3:
print(truth1(False, True, False)) #the answer is false
#4:
print(truth1(False, True, True)) #the answer is false
#5:
print(truth1(True, False, False)) #the answer is false
#6:
print(truth1(True, False, True)) #the answer is true
#7:
print(truth1(True, True, False)) #the answer is true
#8:
print(truth1(True, True, True)) #the answer is true

#Question #2: 
import math
def areaOfCircle(radius):
    area = math.pi * radius**2
    return area
print(areaOfCircle(5))

#Question #3: 
correct_password = "OpenUp"
attempts = 0
while attempts <= 3:
    user_input = input("Enter the password: ")
    if user_input == correct_password:
        print("You have successfully logged in.")
        break
    else:
        attempts += 1
        if attempts > 3:
            print("You have been denied access.")
            break
        else:
            print("Incorrect password. Try again.")

#Question #4: 
#the answer is b: an expression that is either true or false 

#Question #5:
#1: 
#operator: == definition of each operator: equal to
#2:
#operator: != definition of each operator: not equal to
#3:
#operator: > definition of each operator: greater than
#4:
#operator: < definition of each operator: less than
#5:
#operator: >= definition of each operator: greater than or equal to
#6:
#operator: <= definition of each operator: less than or equal to

#Question #6:
"""
for i in [12, 16, 17, 24, 29]:
    if i % 2 == 1: # if the number is odd
        break # immediately exit the loop
    print(i)
print("done")
"""
#answer: the code above will print:
#12
#16
#done

#Question #7:
"""
for i in [12, 16, 17, 24, 29, 30]:
    if i % 2 == 1: # if the number is odd
        continue # don't process it
    print(i)
print("done")
"""
#answer: the code above will print:
#12
#16
#24
#30
#done

#Question #8:
"""
x=5
if x == 5:
    print "Wow, X is EXACTLY five!
elif x > 5:
    print "X is now MORE than five!"
else:
    print "X is now LESS than five!"
"""
#answer: Will not run because there is a syntax error

#Question #9:
"""
def functionA(t, side, num):
    for i in range(num):
        square(t, side)
        t.penup()
        t.forward(side*2)
        t.pendown()
"""
#answer: The code will produce multiple squares drawn in a row, 
# each square separated by a distance equal to twice the length of the side of the square.

#Question #10:
"""
def functionB():
    for i in range(5):
        t.forward(100)
        t.right(72)
"""
#answer: The code will produce a five-pointed star shape.



