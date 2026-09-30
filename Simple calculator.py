"""
Filename: simple_calculator.py
Author: <Merino, Abdul>
Created: <09/28/2026>
Instructor: Burgess
"""
print("Welcome to the Simple Calculator")
print("This calculator will ask the user to input two numbers, then the program will perform the four basic operations on the two numbers (add, subtract, multiply, and divide).")

N1=int(input("please enter the first number: "))
N2=int(input("Please enter the second number: "))

op=(input("Enter the operation(+,-,*,/): "))
if op=="+":
    print(N1+N2)
elif op=="-":
    print(N1-N2)
elif op == "-":
    print(N1*N2)
elif op == "*":
    print(N1*N2)
elif op == "/":
    print(N1/N2)





