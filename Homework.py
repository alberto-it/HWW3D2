"""
Lesson 7: Assignments | Python Exception Handling
1. Exceptional Weather Forecast
Objective: The aim of this assignment is to enhance your understanding of exception handling 
by creating a weather forecast application that gracefully handles unexpected user input 
and provides user-friendly error messages.

Task 1: Start
Begin by setting up a simple user input loop that asks the user to enter the temperature in Fahrenheit.

Ensure that your program only accepts numerical input and provides a friendly error message
if the user enters something that can't be converted to a number.
"""
while True:
    try:
        f_temp = float(input("Enter the temperature in Fahrenheit: "))
        break 
    except ValueError:
        print("Invalid input. Please enter a number.")
"""
Task 2: Temperature Conversion
Write a function that converts the Fahrenheit temperature to Celsius.
Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process, 
such as division by zero or overflow errors.

Task 3: User Experience
Implement an else block that prints the converted temperature in a user-friendly format.

Add a finally block that thanks the user for using the weather forecast application, 
ensuring that this message is displayed regardless of whether an exception was caught or not.
"""
def f_to_celsius(f):
    try:
        c = (f - 32) * 5 / 9
    except ZeroDivisionError:
        print("Error: Division by zero occurred during conversion.")
    except OverflowError:
        print("Error: Number is too large.")
    else:
        print(f"{f}°F is equal to {c:.2f}° Celsius.")
    finally:
        print("Thank you for using the weather forecast application!")

f_to_celsius(f_temp)