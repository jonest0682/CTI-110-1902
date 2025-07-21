# Timothy Jones
# 7/16/2025
# P4HW1
# Score Analyzer

#Begin
# Ask how many scores to enter
num_scores = int(input("How many scores do you want to enter? "))

# Initialize list to store valid scores
valid_scores = []

# Loop to collect scores
for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:
                valid_scores.append(score)
                break
            else:
                print("  INVALID Score entered!!!!")
                print("  Score should be between 0 and 100")
        except ValueError:
            print("  Please enter a valid number.")

# Process scores
lowest = min(valid_scores)
modified_scores = valid_scores.copy()
modified_scores.remove(lowest)
average = sum(modified_scores) / len(modified_scores)

# Determine letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Print results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest}")
print(f"Modified List : {modified_scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")

#End
