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

q2=input("QUESTION" )
if q2 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q3=input("QUESTION" )
if q3 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q4=input("QUESTION" )
if q4 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q5=input("QUESTION" )
if q5 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q6=input("QUESTION" )
if q6 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q7=input("QUESTION" )
if q7 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q8=input("QUESTION" )
if q8 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q9=input("QUESTION" )
if q9 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5

q10=input("QUESTION" )
if q10 == "1":
    print("correct, you've earned one point!")
    sc += 10
    correct_Answer += 1
else:
    print("incorrect, you've lost a point")
    if sc > 0:
        sc -= 5













print(f"correct answers {correct_Answer}/10")
print(f"score {sc}/10")

