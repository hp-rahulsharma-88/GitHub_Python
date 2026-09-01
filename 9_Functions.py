# Function1 Declaration
def myFunction(name):
    print("Hello "+name)
    it = 10
    while it > 1:
        if it == 9:
            it = it - 1  # 8
            continue  # skip the rest of loop execution till line no 13 for this iteration only
        if it == 3:
            break  # jump out from the loop while if condition matches
        print(it)
        it = it - 1

# Function2 Declaration
def addIntegers(num1, num2):
    print("The sum of given numbers is:",num1+num2)
    print("{} {}".format("The sum of two numbers is:", num1+num2))

# Function3 Declaration
def subIntegers(num1, num2):
    return num1-num2


myFunction("Rahul Sharma") # Function1 Calling
print("*************************************")
addIntegers(4, 8) # Function2 Calling
print("*************************************")
subtraction = subIntegers(7, 2) # Function3 Calling
# print("The difference of two numbers is:",subtraction)
print("{} {}".format("The difference of two numbers is:", subtraction))