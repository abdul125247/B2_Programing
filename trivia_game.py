"""
Filename: trivia_game.py
Author: <Merino, Abdul>
Created: <10/05/2026>
Instructor: Burgess
"""
print("Welcome to the Trivia Game!")
print("In just a moment, you’ll be presented with a series of questions.")
print("Please answer each question carefully. Once you’ve completed the quiz, you'll receive a score reflecting how many questions you answered correctly.")

sc = 0
correct_Answer = 0


q1=input("What is the default data type for numbers in Python?" )
if q1 == "int":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q2=input("What is the default data type for decimal numbers in Python?" )
if q2 == "float":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q3=input("Which built-in function is used to display text or output on the screen in Python?" )
if q3 == "print":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q4=input("What keyword is used to start a conditional statement?" )
if q4 == "if":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q5=input("What character is used to start a single-line comment in Python?" )
if q5 == "#":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q6=input("What is the term for a mistake or error in a program's code?" )
if q6 == "bug":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q7=input("What data type is used to represent text in Python?" )
if q7 == "string":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q8=input("What keyword is used to add a fallback or default choice at the very end of an if-statement chain?" )
if q8 == "else":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q9=input("What mathematical operator symbol is used to multiply two numbers in Python?" )
if q9 == "*":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q10=input("What operator symbol is used to divide two numbers in Python?" )
if q10 == "/":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5













print(f"correct answers {correct_Answer}/10")
print(f"score {sc}/100")

