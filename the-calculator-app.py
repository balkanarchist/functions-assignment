# Task 1: Create functions for each (basic) arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Uh-oh! You cannot divide by zero."
    
num1 = float(input("Please input the first number: "))
num2 = float(input("Please input the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Uh oh, Einstein. You cannot divide by zero.\n")