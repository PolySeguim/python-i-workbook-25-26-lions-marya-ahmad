"""
Exercise 108: Negatives, Zeros, and Positives
readIntegers()
Create a program that reads integers from the user until a blank
line is entered.
displayIntegers()
Once all of the integers have been read your
program should display all the negative numbers, followed by all
of the zeros, followed b y all of the positive numbers.
Within each
group the numbers should be displayed in the same order that they were
entered by the user. For example, if the user enters the values
3, -4, 1, 0, -1, 0, and -2 then your program should output the values
-4, -1, -2, 0 ,0 , 3, and 1. Your program should display each value
on its own line.
"""

"""
Exercise 109: List of Proper Divisors
A proper divisor of a positive integer, n, is a positive integer
less than n which divides evenly into n. Write a function that
computes all of the proper divisors of a positive integer. The
integer will be passed to the function as its only parameter.
The function will return a list containing all of the proper divisors
as its only result. Complete this exercise by writing a main program
that demonstrates the function by reading a value from the user and
displaying the list of its proper divisors. Ensure that your main
program only runs when your solution has not been imported into
another file
"""

"""
Exercise 110: Perfect Numbers
An integer, n, is said to be perfect when the sum of all the proper
divisors of n is equal to n. For example, 28 is a perfect number
because its proper divisors are 1, 2, 4, 7, and 14, and 1+2+4+7+14 = 28.
Write a function that determines whether or not a positive integer is
perfect. Your function will take one parameter. If that parameter is a
perfect number then your function will return true. Otherwise it will
return false. In addition, write a main program that uses your
function to identify and display all of the perfect numbers between 1 and
10,000. Import your solution to Exercise 109 when completing this task.
"""

#Exercise 108: Negatives, Zeros, and Positives
def readIntegers():
    integers = []
    while True:
        user_input = input("Enter an integer (or press enter to end): ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            integers.append(number)
        except ValueError:
            print("please enter a valid integer")
    return integers
def displayIntegers(integers):
    negatives = [num for num in integers if num < 0]
    zeros = [num for num in integers if num == 0]
    positives = [num for num in integers if num > 0]
    
    print("Negative numbers:")
    for num in negatives:
        print(num)
    
    print("Zeros:")
    for num in zeros:
        print(num)
    
    print("Positive numbers:")
    for num in positives:
        print(num)

#Excerise 109: List of Proper Divisors
def proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors
def main_109():
    user_input = int(input("Enter a positive integer: "))
    divisors = proper_divisors(user_input)
    print(f"Proper divisors of {user_input} are: {divisors}")

#Exercise 110: Perfect Numbers
def is_perfect(n):
    divisors = proper_divisors(n)
    return sum(divisors) == n
def main_110():
    print("Perfect numbers between 1 and 10,000:")
    for num in range(1, 10001):
        if is_perfect(num):
            print(num)
if __name__ == "__main__":

    #Run excerise 108
    integers = readIntegers()
    displayIntegers(integers)
    
    #Run excerise 109
    main_109()
    
    #Run excerise 110
    main_110()
