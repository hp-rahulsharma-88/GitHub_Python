class Computer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other):
        if c1.age == c2.age:
            return True
        else:
            return False


c1 = Computer("Rahul", 19)
c1.age = 29
c2 = Computer("AC", 29)

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")