# Write a Python program using filter() to extract all even numbers from a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


# Write a program using filter() to select all words from a list that start with a vowel.
words = ["apple", "banana", "orange", "grape", "ice"]
vowels = ("a", "e", "i", "o", "u")
result = list(filter(lambda w: w.lower().startswith(vowels), words))
print(result)


# Given a list of integers, use filter() to remove all negative numbers.
numbers = [-5, 10, -3, 20, -11, 7]
positive = list(filter(lambda x: x >= 0, numbers))
print(positive)


# Write a program using filter() to find numbers greater than 50 from a list.
numbers = [10, 55, 32, 75, 99, 40]
greater_50 = list(filter(lambda x: x > 50, numbers))
print(greater_50)

# Use filter() to extract all palindromic strings from a list.
words = ["level", "python", "hello", "gadag", "world"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)