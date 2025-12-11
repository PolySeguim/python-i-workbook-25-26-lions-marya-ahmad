"""
#Global Variability 

#FUNCTION DECLARATIONS
#void function
def setName(fname):
    #fname is the local function variable
    #f_name is global variable set above
    f_name.set(fname)
    print(f_name)

#fruitful function
def getName():
    return f_name

#function calls
setName("Marya")

#name = getName()
print("Hi", f_name)
"""


"""
sum(list of numbers)
function <- adds up all the numeric values within a list
return int sum
author: Marya (10-08-25)
"""


"""
def sum(numbers):
    sum = 0
    for i in numbers: #[1:len(numbers)]
        sum += i # += ---> sum = sum + i
    return sum
num1 = (1,2,3,4,5,6,7,8.9,10)
test1 = sum(num1)
print(test1)
"""



def absoluteV(x):
    if x < 0: 
        return -x
    return x

def absoluteValue(x):
    if x < 0:
        return -x #the return statement exits the function 
    else:
        return x
    
#AbsoluteValue
print(absoluteValue(-23))

# A fruitful compare function that compares two integers 
# and returns the largest integer 
def compare(a, b):
    if a > b:
        return a
    else:
        return b

# A fruitful hypotenuse function that returns the value of 
# the hypotenuse given the a and b value 
def hypotenuse(a, b):
    return (a**2 + b**2)**0.5


# A fruitful slope function that 
# *** returns the slope of a lime 
# given 4 parameters (x1, y1, x2, y2)
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)
slope(2, 3, 4, 5)

# A fruitful intercept function that will find the y-intercept
# given two points (x1, y1, x2, y2)
# *** This function should call the slope function in order to 
# *** calculate the y-intercept or b-value
def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    b = y1 - m * x1
    return b
intercept(2, 3, 4, 5)


# A fruitful function that will calculate whether a number is 
# a factor of another number 
# *** is 3 a factor of 9?
# *** retrun a boolean value (True or False)
def isFactor(factor, number):
    if number % factor == 0:
        return True
    else:
        return False
isFactor(3, 9)


# A fruitful function that will calculate whether a number is 
# a multiple of another number 
# *** is 12 a multiple of 36
# *** return a BOOLEAN (true or false)
def isMultiple(multiple, number):
    if number % multiple == 0:
        return True
    else:
        return False
isMultiple(12, 36)


#Function Call
