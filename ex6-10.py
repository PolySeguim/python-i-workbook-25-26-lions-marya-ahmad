"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""

"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""

"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""

"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""

"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""

if __name__ == "__main__":
    print("Hi there!");

"""Exercise 6:  Tax and Tip"""
def taxAndTip():
    mealCost = float(input("Cost of your meal: $"))
    taxRate = float(input("Tax rate in your area as a percent:"))
    tax = mealCost * (taxRate / 100)
    tip = mealCost * 0.18
    totalCost = mealCost + tax + tip
    print("The tax on your meal is $", tax)
    print("The tip on your meal is $", tip)
    print("The total cost of your meal is $", totalCost)
taxAndTip()

"""Exercise 7: Sum of the First n Positive Integers"""
def sumOfFirstN():
    n = int(input("Enter a positive integer: "))
    sum = (n*(n + 1))/2
    print("The sum of the first", n, "positive integers is:", sum)
sumOfFirstN() 

"""Exercise 8:  Widgets and Gizmos"""
def widgetsAndGizmos():
    numGizmos = int(input("Number of gizmos in the order:"))
    weightGizmos = numGizmos * 112
    print("The total weight of the order is", weightGizmos, "grams")
widgetsAndGizmos()

"""Exercise 9:  Compound Interest"""
def compoundInterest():
    principal = float(input("Amount of money deposited into the account: $"))
    rate = 0.04
    for year in range(1, 4):
        amount = principal * (1 + rate) ** year
        print("The amount in the savings account after", year, "year(s) is $", format(amount, '.2f'))
compoundInterest()

"""Exercise 10:  Arithmetic"""
import math
def arithmetic():
    a = int(input("Enter an integer (a): "))
    b = int(input("Enter an integer (b): "))
    sum = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    remainder = a % b
    log10a = math.log10(a)
    power = a ** b
    print("The sum of a and b is:", sum)
    print("The difference when b is subtracted from a is:", difference)
    print("The product of a and b is:", product)
    print("The quotient when a is divided by b is:", quotient)
    print("The remainder when a is divided by b is:", remainder)
    print("The result of log10 a is:", log10a)
    print("The result of a to the power of b is:", power)
arithmetic()