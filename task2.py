#"""
x = 5
print(type(x))
x = "Hello"
print(type(x))

class Person:
    creature = "Human"

    def __init__(self, name=None):
        self.name = name
#"""

"""
class Person:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        else:
            self.name = "None"
"""

p1 = Person()
print(type(p1))
# print(p1.name)
# p1 = Person("Karina", 25)
# print(p1.name)
# p1 = Person("Morten")
# print(p1.name)
# print(p1.creature)
# print(p1.__dict__)
# p1.age = 25
# print(p1.__dict__)

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course


# s1 = Student("Morten", "Python")
# print(s1.__dict__)

#"""
class Customer:
    def __init__(self, name, membership):
        self.__name = name
        print("setting name to: " + name)
        self.__membership = membership
        print("setting membership to: " + membership)


# c1 = Customer("Mike", "Gold")
# print(c1.__name)
# print(c1._Customer__name)
#"""

"""
class Customer:
    def __init__(self, name, membership):
        self.name = name
        self.membership = membership
        
        
    @property
    def name(self):
        print("getting name")
        return self._name

    @property
    def membership(self):
        print("getting membership")
        return self._membership


    @name.setter
    def name(self, name):
        print("setting name")
        self._name = name


    @membership.setter
    def membership(self, membership):
        print("setting membership")
        self._membership = membership


c1 = Customer("Mike", "Gold")
print(c1.name)
"""
