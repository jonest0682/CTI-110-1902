# Timothy Jones
# 7/16/2025
# P4LAB2
# Multiplication Table with Loop Control

#begin

run_program = "yes"

while run_program.lower() == "yes":
    try:
        number = int(input("Enter an integer: "))
        
        if number < 0:
            print("\nThis program does not handle negative numbers.\n")
        else:
            print()
            for i in range(1, 13):
                print(f"{number} * {i} = {number * i}")
            print()
    
    except ValueError:
        print("\nInvalid input. Please enter a valid integer.\n")
        continue

    run_program = input("Would you like to run the program again? ").lower()
    print()

print("Exiting program...")

#end
