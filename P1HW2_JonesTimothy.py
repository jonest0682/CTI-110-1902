# Timothy Jones
# 7/5/2025
# P1HW2
# Create a program that does some basic math on numbers that are entered.


#Begin
#Page header
print("This program calculates the display travel expenses\n")

#Integers
budget = int(5400)
destination = ""
gas = int(300)
accomodations = int(750)
food = int(200)
remaining = budget - gas - accomodations - food

# Ask user to enter their budget
print("Enter Budget: 5400 \n")

# Ask user to enter travel destination
print("Enter your travel destination: ", "Chicago\n")

# Ask user for amount they will spend on gas
print("How much do yo think you will spend on gas? ", gas, "\n")

# Ask user for amount they will spend on accommodation
print("Aproximately, how much will you need for accommodation/hotel? ", accomodations, "\n")

# Ask user for amount they will spend on food
print("Last, how much do you need for food? ", food, "\n")

#Travel Expenses breakdown
print("------------Travel Expenses---------------\n")
print("Location: Chicago")
print("Initial Budget: ", budget)

#Deductions
print("Fuel: ", gas)
print("Accomodation: ", accomodations)
print("Food: ", food)

#Total
print("Remaining Balance:", remaining)
#End
