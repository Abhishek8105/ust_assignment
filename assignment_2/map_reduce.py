# How does the map() function work in Python? Give an example where you square each number in a list.
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)


# What is the output of the following code?
from functools import reduce
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(result)
# 24


# How would you use the map() function to convert all string elements of a list to uppercase?
words = ["apple", "banana", "mango"]
upper_case = list(map(str.upper, words))
print(upper_case)

# Write a Python program that uses reduce() to find the greatest common divisor (GCD) of a list of numbers.
from functools import reduce
from math import gcd

def gcd_list(nums):
    return reduce(gcd, nums)

numbers = [24, 60, 36]
print(gcd_list(numbers))

# Compare and contrast the map() and filter() functions in Python.
nums = [1, 2, 3, 4, 5, 6]

list(map(lambda x: x*x, nums))

list(filter(lambda x: x % 2 == 0, nums))