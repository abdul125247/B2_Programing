"""
Merino_Abdul

10/09/2026

Teacher:Burgees

MP1_exam
"""
#C=(F-32) * 5/9

print("welcome to the temperature converter")

temp=float(input("Enter the temperature in Fahrenheit (F): "))

c = ((temp-32)*(5/9))
print(f"{c}°C")

if c >32:
    print("Heat warning!")

elif c <= 0:
    print("freezing alert!")

else:
    print("Normal temperature!")







