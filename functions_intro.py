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

