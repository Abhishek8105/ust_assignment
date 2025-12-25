# How can you add a new key-value pair to an existing dictionary in Python?
student = {"name": "Abhishek", "age": 21}
student["grade"] = "A"
print(student)


# What happens if you try to access a key that does not exist in a dictionary?
data = {"a": 10}
print(data["b"])
# KeyError: 'b'


# Write a Python function that takes a dictionary and returns a list of keys that have values greater than 50.
def greater_50(d):
    result = []
    for key, value in d.items():
        if value > 50:
            result.append(key)
    return result
marks = {"math": 45, "english": 72, "science": 88, "history": 40}
print(greater_50(marks))


# How would you iterate over both keys and values of a dictionary in Python?
d = {"a": 1, "b": 2, "c": 3}
for key, value in d.items():
    print(key, value)


# Write a Python function that merges two dictionaries.
def merge_dict(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

a = {"x": 10, "y": 20}
b = {"y": 30, "z": 40}
print(merge_dict(a, b))
