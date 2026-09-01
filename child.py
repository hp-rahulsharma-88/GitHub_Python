from oops import FirstClass


class childish(FirstClass):
    var = 25
    # calling parent class constructor (if it is not default) from child class constructor
    def __init__(self):
        FirstClass.__init__(self,3, 9)

    def autocompleted(self):
        return self.var + self.number + self.summation()

    def parental(self):
        return self.var + self.number

obj3 = childish()
print("The sum of var and number is:",obj3.parental()) #
print(obj3.autocompleted())