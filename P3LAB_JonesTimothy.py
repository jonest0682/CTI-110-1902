# Timothy Jones
# 7/15/2025
# P3LAB
# "Branching" Assignment tests student's knowledge of how to write
# code that displays information to users

#begin

# set ammount as a float
amount = float(input("Enter the amount of money as a float: $"))

# create cents value (integer) 
cents = int(round(amount * 100))

if cents == 0:
    print("No change")
else:
# list of coin types
    coins = [
        (100, "Dollar", "Dollars"),
        (25, "Quarter", "Quarters"),
        (10, "Dime", "Dimes"),
        (5, "Nickel", "Nickels"),
        (1, "Penny", "Pennies")
    ]
    for value, single, plural in coins:
        count = cents // value
        if count > 0:
# clarify single/plural
            name = single if count == 1 else plural
            print(f"{count} {name}")
            cents -= count * value

            
#end
