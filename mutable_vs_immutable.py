# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 11:13:46 2021
mutable_vs_immutable.py
@author: kales
"""

print("Creating tuple2 with 4, 6, 2, 8, 3, 1, 2")
tuple2 = (4, 6, 2, 8, 3, 1, 2)
print("Contents of tuple2", tuple2)
print("Object ID tuple2", id(tuple2))

print("\nAdding a 9 to the end of tuple2")
tuple2 = tuple2 + (9,)
print("Contents of tuple2 after adding the 9", tuple2)
print("Object ID tuple2", id(tuple2))
print("Did you notice that tuple2 object ID has changed?")

print("\nConvert tuple2 to a list called list1")
list1 = list(tuple2)

print("\nContents of list1", list1)
print("Object ID of list1", id(list1))

print("\nAppend 30 to the end of list1")
list1.append(30)
print("Contents of list 1 after appending 30", list1)
print("Object ID list1", id(list1))
print("Did you notice that the list1 object ID remains the same?")

print("\n\nConclusion: The object ID shows what we really mean by mutable")
print("versus immutable. Mutable objects like list1 keep the same object ID")
print("even after you change their contents. Immutable objects get a new")
print("object ID any time we make a change to their contents. Remember that")
print("it is the object ID that matters.")