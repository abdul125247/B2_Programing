"""
Filename: <avarage_calculator>
Author: <Merino, Abdul>
Created: <10/23/2026>
Instructor: Burgess
"""
sum_of_numbers = 0
number_of_entries=0
average=0

while True:
    num = (int(input("Enter a number!: ")))
    sum_of_numbers = sum_of_numbers + num
    number_of_entries = number_of_entries + 1

    average = sum_of_numbers / number_of_entries

    print(f"your current sum is {sum_of_numbers}")
    print(f"your current number entries is {number_of_entries}")
    print(f"your current average is {average}")
    A=input("do you want to enter another number? y/n ")

    while (A != "y" and A != "n"):
        print("Invalid Input")
        A = input("Do you want to enter another number? y/n ")

    if A=="y":
        continue

    elif A=="n":
        break



