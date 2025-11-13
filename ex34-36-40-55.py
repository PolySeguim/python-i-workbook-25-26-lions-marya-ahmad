"""
Exercise 34: Even or Odd?
Write a program that reads an integer from the user.
Then your program should display a message indicating whether
the integer is even or odd
"""

"""
Exercise 36: Vowel or consonant
In this exercise you will create a program that reads a letter
of the alphabet from the user. If the user enters a, e, i, o, or u
then your program should display a message indicating that the
entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and
sometimes y is a consonant. Otherwise your program should display
a message indicating that the letter is a consonant.
"""

"""
Exercise 40: Name that triangle
A triangle can be classified based on the lengths of its sides as
equilateral, isosceles, or scalene. All 3 sides of an equilateral
triangle have the same length. As isosceles triangle has two sides
that are the same length, and a third side that is a different length.
If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the
user. Display a message indicating the type of triangle
****** CHALLENGE:
Perform the same task as above but with angles and not sides.
"""

"""
Exercise 55: Cell Phone Bill
A particular cell phone plan includes 50 minutes of air time and
50 text messages for $15.00 a month. Each additional minute of
air time costs $0.25 , while additional text messages cost $0.15
each. All cell phone bills include an additional charge of $0.44
to support 911 call centers, and teh entire bill (including the
911 charge) is subject to a 5 percent sales tax.
Write a program that reads the number of minutes and text messages
used in a month from the user. Display the base charge, additional
minutes charge (if any), additional text message charge (if any),
the 911 fee, tax and total bill amount. Only display the additional
minute and text charges if the user incurred costs in these
categories. Ensure that all of the charges are displayed using 2
decimal points
"""

"""Exercise 34: Even or Odd?"""
def even_odd():
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        print("The number is even")
    else: 
        print("The number is odd")
even_odd()

"""Exercise 36: Vowel or consonant"""
def vowel_consonant():
    letter = input("Enter a letter: ")
    if letter in "aeiouAEIOU":
        print("The letter is a vowel")
    elif letter == "yY":
        print("Sometimes y is a vowel, and sometimes y is a consonant")
    else:
        print("The letter is a consonant")
vowel_consonant()

"""Exercise 40: Name that triangle: sides"""
def classify_triangle_by_sides(a, b, c):
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
a = float(input("Side a: "))
b = float(input("Side b: "))
c = float(input("Side c: "))
classify_triangle_by_sides(a, b, c)


"""Exercise 40: Name that triangle: angles"""
def classify_triangle_by_angles(x, y, z):
    if x + y + z != 180:
        print("Not a valid triangle")
    elif x == y == z:
        print("Equilateral triangle")
    elif x == y or y == z or x == z:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
x = float(input("Angle x: "))
y = float(input("Angle y: "))
z = float(input("Angle z: "))
classify_triangle_by_angles(x, y, z)


"""Exercise 55: Cell Phone Bill"""
def calculate_cell_phone_bill(minutes_used, texts_used):
    base_charge = 15.00
    extra_min_charge = 0.25 * max(0, minutes_used - 50)
    extra_text_charge = 0.15 * max(0, texts_used - 50)
    emergency_fee = 0.44
    subtotal = base_charge + extra_min_charge + extra_text_charge + emergency_fee
    tax = subtotal * 0.05
    total = subtotal + tax
    print(f"Base charge: ${base_charge:.2f}")
    if extra_min_charge > 0:
        print(f"Additional minutes charge: ${extra_min_charge:.2f}")
    if extra_text_charge > 0:
        print(f"Additional text message charge: ${extra_text_charge:.2f}")
    print(f"911 fee: ${emergency_fee:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total bill: ${total:.2f}")
minutes = int(input("Minutes used: "))
texts = int(input("Text messages used: "))
calculate_cell_phone_bill(minutes, texts)


