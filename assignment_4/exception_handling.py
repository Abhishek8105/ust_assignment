# Write a Python program to handle a ZeroDivisionError.
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



# Write a program that accepts user input and handles a ValueError if the input is not an integer.
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Error: Please enter a valid integer.")



# Write a program to open a file and handle a FileNotFoundError.
try:
    filename = input("Enter file name: ")
    file = open(filename, "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File not found.")



# Write a Python program that uses try, except, else, and finally blocks.
try:
    num = int(input("Enter a number: "))
    print("Square:", num * num)

except ValueError:
    print("Error: Invalid number.")

else:
    print("Execution successful — no exceptions occurred.")

finally:
    print("Program ended (finally block executed).")



# Write a program to handle multiple exceptions in a single try block.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ValueError:
    print("Error: Please enter only integers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print("Unexpected Error:", e)