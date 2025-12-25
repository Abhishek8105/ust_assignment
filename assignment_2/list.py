# How do you add an element at the end of a list in Python?

lst = [1, 2, 3]
lst.append(4)
print(lst)

# How can you remove an element from a list by its index?

lst = [10, 20, 30, 40]
lst.pop(2)
print(lst)


# What will be the output of the following code snippet?

lst = [1, 2, 3, 4, 5]
lst[1:3] = [10, 20]
print(lst)

# output : [1, 10, 20, 4, 5]

# How can you check if an element exists in a list in Python?

lst = [5, 10, 15]

if 10 in lst:
    print("Element found")

# Write a Python function that removes duplicates from a list without using the set() function.

def remove_duplicates(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))
