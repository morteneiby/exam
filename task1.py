# String 'Hello' eller "Hello" "Det er John's bil" 'John sagde: "Hej"'
# int = heltal - float = kommatal
# bool = komplet system til logiske operationer, udtrykkes som sandt eller falsk.

listA = [1, 2, 'A', 'B', 1, 2, 'A', 'B']
# Ordnet, kan ændres, duplikerede værdier
print(listA[0])
print(listA[-1])
print(listA[2:5])
# listA[2] = 'C'
# print(listA)
# listA.insert(4, 'C')
# print(listA)
# .append('C') - .extend(tupleB) - .remove('C') - .pop(1) - .count('A') - .index('B')
# len() - list()
# del - .clear()
# print(listA)


tupleB = (1, 2, 'A', 'B', 1, 2, 'A', 'B')
# Ordnet, kan ikke ændres, duplikerede værdier
# print(tupleB[0])
# print(tupleB[-1])
# print(tupleB[2:5])
# tupleB[2] = 'C' - NOT
# tupleToList = list(tupleB) - tupleB = tuple(tupleToList)
# .count('A') - .index('B')
# len() - tuple()
# del - .clear()


setC = {1, 2, 3, 4, 'A', 'B', 'C', 'D'}
# ikke ordnet, kan ikke ændres, kan ikke indeholde duplikerede værdier
# setC.add('E')
# .update(tupleB) - .remove('A') - .discard('B') - .pop() - -clear()
# .union() - .update() - .intersection_update() - .symmetric_difference_update()
# len()
# del - .clear()
# print(setC)


dictD = {"brand": "Honda", "model": "NC700X", "year": 2013, "electric": False, "colors": ["red", "black"]}
# nøgle : værdi
# Ordnet, kan ændres, kan ikke indeholde duplikerede værdier
# len()
# print(dictD["model"])
# .get("model") - .keys() - .values() - .items()
# dictD["year"] = 2012 - dictD.update({"year": 2012})
# dictD["type"] = "touring" - dictD.update({"type": "touring"})
# .pop("model") - .popitem()
# del - .clear()
# print(dictD)


# Loops
# for i in listA:
#   print(i)

# for i in range(len(listA)):
#   print(listA[i])

# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# Comprehension
# listName = [expression for item in iterable if condition == True]
# listB = [x for x in listA if x != 'A']
# print(listB)

# Functions
# def function1():
#    print("Hello, World")


# def function2(name):
#     print("Hello, " + name)


# function1()
# function2("Morten")

