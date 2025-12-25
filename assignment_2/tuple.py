# Can you modify the elements of a tuple after it has been created? Why or why not?
# No — tuples are immutable.


# How would you access the second-to-last element in a tuple?
t = (10, 20, 30, 40, 50)
print(t[-2])


# What is the difference between a list and a tuple in Python?
lst = [1, 2, 3]   # list : mutable
t = (1, 2, 3)     # tuple : immutable

# Given the tuple t = (1, 2, 3, 4), how can you change the value 3 to 100?
t = (1, 2, 3, 4)

temp = list(t)
temp[2] = 100
t = tuple(temp)

print(t)



# Write a Python function that takes a tuple of numbers and returns the sum of all its elements.
def sum_tuple(t):
    total = 0
    for n in t:
        total += n
    return total

t = (5, 10, 15)
print(sum_tuple(t))
