"""
Exercise 51:  Letter Grade to Grade Points

At a particular university, letter grades are mapped to grade
points in the following manner:

Letter                  Grade points
A+                      4.0
A                       4.0
A-                      3.7
B+                      3.3
B                       3.0
B-                      2.7
C+                      2.3
C                       2.0
C-                      1.7
D+                      1.3
D                       1.0
F                       0


Write a program that begins by reading a letter grade from the 
user.  Then your program should compute and display the equivalent
number of grade points.  Ensure that your program generates an 
appropriate error message if the user enters an invalid letter
grade.
"""


"""
Exercise 52:  In the previous exercises you created a program that
converts a letter grade into the equivalent number of grade points.
In this exercise you will create a program that reverses the process
and converts from a grade point value entered by the user to a letter
grade.  Ensure that your program handles grade point values that fall
between letter grades.  These should be rounded to the closes letter
grade.  Your program should report A+ for a 4.0 (or greater) grade
point average.
"""

"""
Exercise 66:  Compute a Grade Point Average
Exercise 51 includes a table that shows the conversion from letter
grades to grade points at a particular academic institution.  In this
exercise you will compute the grade point average of an arbitrary number
of letter grades entered by teh user.  The user will enter a blank
line to indicate that all of the grades have been provided.  For example,
if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solutions to Exercise 51 helpful when completing this 
exercise.  Your program does not need to do any error checking.  It can
assume that each value entered by the user will be a valid letter grade
or a blank line.
"""

"""Exercise 51: Letter Grade to Grade Points"""
def letter_grade():
    grade = input("Letter grade: ")
    if grade == "A+" or grade == "A":
        print("4.0")
    elif grade == "A-":
        print("3.7")
    elif grade == "B+":
        print("3.3")
    elif grade == "B":
        print("3.0")
    elif grade == "B-":
        print("2.7")
    elif grade == "C+":
        print("2.3")
    elif grade == "C":
        print("2.0")
    elif grade == "C-":
        print("1.7")
    elif grade == "D+":
        print("1.3")
    elif grade == "D":
        print("1.0")
    elif grade == "F":
        print("0")
    else:
        print("Invalid letter grade")
letter_grade()

"""Exercise 52: Grade Points to Letter Grade"""
def grade_points():
    points = float(input("Grade points: "))
    if points >= 4.0:
        print("A+")
    elif points >= 3.7:
        print("A-")
    elif points >= 3.3:
        print("B+")
    elif points >= 3.0:
        print("B")
    elif points >= 2.7:
        print("B-")
    elif points >= 2.3:
        print("C+")
    elif points >= 2.0:
        print("C")
    elif points >= 1.7:
        print("C-")
    elif points >= 1.3:
        print("D+")
    elif points >= 1.0:
        print("D")
    else:
        print("F")
grade_points()

"""Exercise 66: Compute a Grade Point Average"""
def calculate_gpa():
    total = 0
    count = 0
    while True:
        grade = input("Enter a letter grade (blank to finish): ")
        if grade == "":
            break
        if grade == "A+" or grade == "A":
            total += 4.0
        elif grade == "A-":
            total += 3.7
        elif grade == "B+":
            total += 3.3
        elif grade == "B":
            total += 3.0
        elif grade == "B-":
            total += 2.7
        elif grade == "C+":
            total += 2.3
        elif grade == "C":
            total += 2.0
        elif grade == "C-":
            total += 1.7
        elif grade == "D+":
            total += 1.3
        elif grade == "D":
            total += 1.0
        elif grade == "F":
            total += 0.0
        count += 1
    if count > 0:
        print("Grade Point Average:", round(total / count, 1))
    else:
        print("No grades entered.")
calculate_gpa()
