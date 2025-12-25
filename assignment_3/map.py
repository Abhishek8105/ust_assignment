# Write a Python program using map() to convert a list of integers into their squares.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


# Write a program using map() to convert all strings in a list to uppercase.
words = ["python", "map", "function"]
upper_words = list(map(str.upper, words))
print(upper_words)


# Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.
c = [0, 10, 25, 37]
f = list(map(lambda c: (c * 9/5) + 32, c))
print(f)


# Write a program using map() to calculate the length of each word in a list of strings.
words = ["apple", "banana", "kiwi", "grapes"]
lengths = list(map(len, words))
print(lengths)

# Use map() to add 10 to each element of a given list of numbers.
numbers = [5, 10, 15, 20]
result = list(map(lambda x: x + 10, numbers))
print(result)
