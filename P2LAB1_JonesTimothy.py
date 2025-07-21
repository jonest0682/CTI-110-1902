# Timothy Jones
# 7/13/2025
# P2LAB1
# "Variables and Expressions", Assignment tests student's knowledge of how to write code
# that performs mathematical calculations and displays information to users


#begin
import math

# use radius as a float
radius = float(input("What is the radius of the circle? "))

# Calculate values
# diameter
diameter = 2 * radius
# circumference
circumference = 2 * math.pi * radius
# area
area = math.pi * radius ** 2

# print results 
print(f"The diameter of the circle is {diameter:.1f}") #diameter
print(f"The circumference of the circle is {circumference:.2f}") #circumference
print(f"The area of the circle is {area:.3f}") #area

#end
