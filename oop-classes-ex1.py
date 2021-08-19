# Class methods, calling a class

class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def output_num_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


class Math:

    @staticmethod #static class methods that do not change anything, but can be called to do a function.
    def add5(x):
        return x + 5


p1 = Person('Tim')
p2 = Person('Kevin')
print(Person.output_num_of_people())
print(Math.add5(3))