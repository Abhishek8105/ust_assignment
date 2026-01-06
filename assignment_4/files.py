# Write a Python program to create a text file and write multiple lines into it.
lines = [
    "This is line one.\n",
    "This is line two.\n",
    "This is line three.\n"
]

with open("sample.txt", "w") as file:
    file.writelines(lines)

print("File created and lines written successfully.")



# Write a program to read the contents of a text file line by line.
with open("sample.txt", "r") as file:
    for line in file:
        print(line, end="")



# Write a Python program to count the number of lines, words, and characters in a text file.
lines = words = characters = 0

with open("sample.txt", "r") as file:
    for line in file:
        lines += 1
        words += len(line.split())
        characters += len(line)

print("Total Lines     :", lines)
print("Total Words     :", words)
print("Total Characters:", characters)



# Write a program to copy the contents of one text file into another file.
source = "sample.txt"
destination = "copy_sample.txt"

with open(source, "r") as src, open(destination, "w") as dest:
    for line in src:
        dest.write(line)

print("File copied successfully.")



# Write a Python program to search for a specific word in a text file and display the line numbers where it appears.
word = input("Enter the word to search: ")
line_no = 0
found = False

with open("sample.txt", "r") as file:
    for line in file:
        line_no += 1
        if word in line:
            print(f"Word found in line {line_no}: {line.strip()}")
            found = True

if not found:
    print("Word not found in file.")
