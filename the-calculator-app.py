# Task 1: Create functions for each (basic) arithmetic operation.
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
    
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.