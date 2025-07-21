# Timothy Jones
# 7/13/2025
# P2HW2
# Create a program that does some basic math on numbers that are entered.


#Begin
#Page header
print("This program calculates the display travel expenses\n")

# Travel Expenses Program

# User input
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

#New assignment add

# Output travel expenses
print("\n------------Travel Expenses------------")
print(f"{'Location:':20s}{destination}")
print(f"{'Initial Budget:':20s}${budget:.2f}")
print(f"{'Fuel:':20s}${gas:.2f}")
print(f"{'Accomodation:':20s}${hotel:.2f}")
print(f"{'Food:':20s}${food:.2f}")
print("----------------------------------------")
print(f"\nRemaining Balance: ${remaining_balance:.2f}")

#End
