import math

# Type hinting is optional, but recommended as it improves code readability and checking for type mismatches later.
number: int = 100
decimal: float = 3.141569
string: str = "Isaac"
complex_number: complex = complex(1, 2)
boolean: bool = True

# Type casting
number2: int = int(decimal)# Default behaviour is equivalent to that of floor().
ceilNumber: int = math.ceil(decimal)
floorNumber: int = math.floor(decimal)
print(number2)
print(ceilNumber)
print(floorNumber)

# Python has type hinting, NOT type enforcement. For the below example, it doesn't enforce the hinted type.
number3: float = int(decimal)

"""
Collections

For each collection:
 - Create empty collection
 - Modify collection
 - Check for existence of an element in the collection
 - Try to mimic the pass by reference example
 - Create a copy
 - Merge the collections
 - Iterate through the collection
"""

# list

# Empty list
lst0: list = list()

lst1: list = [1, 2, 3]
print(len(lst1))
print(lst1)
lst1.append(4)
print(lst1)

# Merge two lists.
lst2 = [7, 8, 9]
lst3: list = lst1 + lst2
print(lst3)

# CAUTION: Collections are passed by reference!!
lst4: list = lst3
lst4[0] = 10
print(f"lst3: {lst3}")
print(f"lst4: {lst4}")

lst4: list = list(lst3)
lst4[0] = 11
print(f"lst3: {lst3}")
print(f"lst4: {lst4}")

# Delete an element
del lst3[0]
print(lst3)

if 10 in lst3:
    print("10 is present in lst3!")
else:
    print("10 is not present in lst3!")

# Iterating through the list.
for element in lst3:
    print(element)

for index in range(len(lst3)):
    print(lst3[index])

for index, element in enumerate(lst3):
    # print(index + ":" + element)
    print(f"{index}:{element}")

print(enumerate(lst3))


# Dictionary
dict0: dict = dict()

# The keys in a dictionary have to be unique, but not the values.
dict1: dict = {
    "key1": 1,
    "key2": 2,
}
print(dict1)

# Update the value for an existing key.
dict1["key1"] = 11
print(dict1)

# Add a new key-value pair.
dict1["key3"] = 3
print(dict1)

# Delete a key-value pair
del dict1["key1"]
print(dict1)

# Check for existence of a key.
if "key1" in dict1:
    print("key1 found in dictionary!")
else:
    print("key1 not found in dictionary!")

# Check for existence of a value.
if 2 in dict1.values():
    print("Value 2 found in dictionary!")
else:
    print("Value 2 not found in dictionary!")

# BEWARE pass by reference!
dict2: dict = dict1
dict2["key10"] = 10
print(dict1)
print(dict2)

dict3: dict = dict(dict1)
dict3["key11"] = 11
print(dict1)
print(dict3)

# Merging two dictionaries
dict4: dict = {
    "key10": 1010101010,
    "key11": 11,
    "key12": 12
}
dict5: dict = dict(dict1)
dict5.update(dict4)
print(dict1)
print(dict5)

# Iterating through dictionaries
for element in dict5:
    print(element)

for key, value in dict5.items():
    print(f"{key}: f{value}")
 

"""
Collections

For each collection:
 - Create empty collection
 - Modify collection
 - Check for existence of an element in the collection
 - Try to mimic the pass by reference example
 - Create a copy
 - Merge the collections
 - Iterate through the collection
"""
#todo create an empty collection of set, tuple and frozenset
#todo check for the existence of an element in the collection
#todo try to mimic the pass by reference example
#todo create a copy of the collecction
#todo merge the collections
#todo iterate through the  collection

#Set
#Set's are unordered and do not allow duplicates
# 1 and True are equal
# elements can't be accessed with indexes
myset = set()
print(type(myset))

myset = {"Car", True, False}

""":"""

thisset = myset.copy()   #copying
thisset.add("Orange")
print(f"thisset: {thisset}")
print(f"myset: {myset}")

union_set = thisset.union(myset) #using the underscore convention for naming variables.
newset = thisset.copy()
print(f"union_set: {union_set}")
print(f"newset: {newset}")

for item in union_set: #using full description instead of one letter
    print(item)

#update method can be used to combine two sets or even add elements of a list to a set
#remove and element of the set by using remove(element) or discard()
#clear() empties the set and del() deletes the entire set
#pop() removes the last element of the set which is weird to use because set elements are unordered

#Questions:
print("Car" in myset)
set()
#difference between using set() and using copy()
#why does set() act as a constructor and a means to copy?
#why does copying with set() create a different reference address?

#tuple
#They are ordered, unchangeable and allow duplicate values
# we cannot add or remove items after the tuple has been created
# The order will not change throughout the lifetime of the tuple
# tuples have the capability of packing and unpacking


mytuple = ("Hey", 1, False, True, "Hey")
print(mytuple)
print(f"tuple length: {len(mytuple)}")

#to create a tuple with one item, you have to add a comma after the item
onetuple = ("apple",)
print(type((onetuple)))

#empty tuple
emptytuple = tuple()
print(type(emptytuple))

#accessing an element in a tuple
print(mytuple[2])

#confirming pass by reference
byreftuple = mytuple
print("Confirming pass by ref ")
print(byreftuple.index(False))
print(mytuple.index(False)) #same index
print(byreftuple)

byreftuple = tuple(mytuple) #it doesn't print reference addresses like in java so I cant really tell if a new reference has been created especially because tuples are unchangeable
print(byreftuple)

#join 2 tuples
tuple1 = ("Apple", "Orange", "Pineapple ")
tuple2 = ("She ", "wants", "me")
tuple3 = tuple1 + tuple2
print(f"this is tuple3: {tuple3}")

#iteration
print("Items in mytuple")
for item in mytuple:
    print(item)


#frozenset
print(f"frozensets: ")
#empty
firstfrozenset = frozenset()

#cannot be modified

#accessing an element of the frozenset
myfset = frozenset(('a','e','i','o','u'))

#when using frozen sets, use '' instead of ""
#addditionally you cannot access elements of a frozen set since its unordered like a set.

#mimic the pass by reference
otherfset = myfset
newfset = (1,2,3,4,5)
otherfset = otherfset.union(newfset)
print(otherfset)
print(myfset)
# doesn't seem to be pass by reference since it didn't remain the same after the union operation

#frozen sets have the .copy() method.

#iteration
for item in otherfset:
    print(item)

lst1 = [1,2,3]
lst2 = [1,2,3]
lst3 = lst1
lst4 = list(lst1)
print(id(lst1) == id(lst2))
print(id(lst1) == id(lst3))
print(id(lst1) == id(lst4))


