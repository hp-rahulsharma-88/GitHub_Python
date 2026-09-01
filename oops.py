class FirstClass:
    number = 22 # Class Variables or Class Attribute which is constant for each object of a class

    # default parameterized Constructor called when object is created of a class
    def __init__(self, num1, num2):
        # Instance Variable or Attributes - which may changed for each object of a class while creating object
        self.number1 = num1
        self.number2 = num2
        print("Default Constructor called when object is created for the respective class")

    def method(self):
        print("Function defined in class is treated as Method")
        #print("Also the number value is ",number)
        print(self.number)

    def summation(self):
        return self.number1 + self.number2 + self.number



obj = FirstClass(3, 4) # create object of class FirstClass, calling default parameterized constructor
obj.method() # calling class method using object
print("Number value is",obj.number)
print("Sum of values is for first object",obj.summation())

obj1 = FirstClass(5,9) # create object of class FirstClass, calling  default parameterized constructor
obj1.method() # calling class method using object
print("Number value is",obj1.number)
print("Sum of values is for second object",obj1.summation())