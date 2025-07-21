# Timothy Jones
# 7/15/2025
# P3HW1
# "Debug" This program takes a number grade, determines average, and displays letter grade for average.

#Begin
# Collecting six module grades
grades = []

grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

#Calculations
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

#Print results
print("\n------------Results------------")
print(f"{'Lowest Grade:':20s}{lowest}")
print(f"{'Highest Grade:':20s}{highest}")
print(f"{'Sum of Grades:':20s}{total}")
print(f"{'Average:':20s}{average:.2f}")
print("--------------------------------")

# Determine letter grade for average
print("\nLetter Grade:")

if average >= 90:
    print("Your grade is: A")
elif average >= 80:
    print("Your grade is: B")
elif average >= 70:
    print("Your grade is: C")
elif average >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")

#End


