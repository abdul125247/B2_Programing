"""
Filename: conditional_calculator.py
Author: <Merino, Abdul>
Created: <09/29/2026>
Instructor: Burgess
"""
print("Welcome to the Conditional Calculator")
print("This calculator will ask the user to input two numbers and an operation then the program will perform one of the four basic operations on the two numbers (add, subtract, multiply, and divide).")

N1=int(input("please enter the first number: "))
N2=int(input("Please enter the second number: "))

op=(input("Enter the operation(+,-,*,/): "))
if op=="+":
    print(f"{N1}+{N2}={N1+N2}")
elif op=="-":
    print(f"{N1}-{N2}={N1-N2}")
elif op == "*":
    print(f"{N1}*{N2}={N1*N2}")
elif op == "/":
    print(f"{N1}/{N2}={N1/N2}")
