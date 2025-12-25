# How do you remove all elements from a set in Python?
s = {1, 2, 3}
s.clear()
print(s)

# What is the output of the following code snippet?

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a - b)
# {1, 2}


# How do you check if an element is present in a set?
s = {10, 20, 30}
if 20 in s:
    print("Element exists")


# Write a Python program to find the intersection of two sets.
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
intersection = a.intersection(b)
print(intersection)


# How does a set handle duplicate values when adding them?
s = {1, 2, 3}
s.add(2)
print(s)