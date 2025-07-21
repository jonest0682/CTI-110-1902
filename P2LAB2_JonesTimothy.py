# Timothy Jones
# 7/13/2025
# P2LAB2
# "Dictionary" Assignment tests student's knowledge of how to write code
# that uses a dictionary to store user input and displays output to the user.


#begin

#create dict
vehicle_mpg = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}
#keys
keys = vehicle_mpg.keys()
print(keys)

#vehicle - output
vehicle = input("Enter a vehicle to see its mpg: ")

#MPG - output
mpg = vehicle_mpg[vehicle]
print(f"\nThe {vehicle} gets {mpg} mpg.")

#miles - float for miles to drive
miles = float(input(f"\nHow many miles will you drive the {vehicle}? "))

#gallons needed to drive
gallons_needed = miles / mpg

#print result
print(f"\n{gallons_needed:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")

#end
