from time import sleep

# Interators
names = ["Karina", "Rasmus", "Hubert", "Andreas"]

for x in names:
    print(x)

"""
def getData(data):
    dataList = []
    for i in range(len(data)):
        sleep(.75)
        print(i)
        dataList.append(data[i])
    return dataList

print(getData(names))


li = iter(names)
print(li.__next__())
print(next(li))
"""
"""
class MyIterator:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

numbers = MyIterator()

print(next(numbers))
#for i in numbers:
#    print(i)
"""

"""
# Generator
def useGenerator():
#    return 5
#    yield 5
    yield 1
    yield 2
    yield 3


values = useGenerator()

#print(values)
#print(values.__next__())
#print(values.__next__())

#for i in values:
#    print(i)
#    sleep(.75)


def sqTopten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


val1 = sqTopten()

for j in val1:
    print(j)

val2 = sqTopten()
print(list(val2))
"""
#Decorators
"""
def decoratorFunction(massage):
    def wrapperFunction():
        print(massage)
    return wrapperFunction

hiFunc = decoratorFunction('Hi')
byeFunc = decoratorFunction('Bye')

hiFunc()
byeFunc()
"""

def decoratorFunction(originalFunction):
    def wrapperFunction():
        return originalFunction()
    return wrapperFunction

"""
def display():
    print('massage from display function ')


decoratedDisplay = decoratorFunction(display)

decoratedDisplay()
"""
"""
@decoratorFunction
def display():
    print('massage from display function ')


display()
"""
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
# Context Manager

"""
class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('sample.txt', 'w') as f:
    f.write('Testing')
   
print(f.closed)
"""
"""
from contextlib import contextmanager

@contextmanager
def openFile(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()

with openFile('sample.txt', 'w') as f:
    f.write('Testing3')

print(f.closed)
"""