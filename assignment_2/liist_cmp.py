# Write a list comprehension that returns all even numbers from 0 to 20.
evens = [x for x in range(21) if x % 2 == 0]
print(evens)


# How would you create a new list of squares from an existing list of numbers using list comprehension?
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(squares)


# Write a list comprehension to extract all words that are longer than 4 characters from a sentence.
sentence = "list comprehension to extract all words"
words = [w for w in sentence.split() if len(w) > 4]
print(words)


# How can you use list comprehension to generate a list of the first 10 Fibonacci numbers?
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(fib[:10])


# Can you use an if condition inside a list comprehension? Provide an example where only odd numbers are selected from a list.
nums = [1, 2, 3, 4, 5, 6, 7]
odds = [x for x in nums if x % 2 != 0]
print(odds)