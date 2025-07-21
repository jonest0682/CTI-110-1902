# Timothy Jones
# 7/13/25
# P2HW2
# Assignment assess student understanding of Lists
# asks the user to enter grades for tests

#begin
# ---------------------Comments in Pseudocode ---------------------

#Grades list
grades = []

#Input grades
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))


grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

#Grade calculations
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

#end
