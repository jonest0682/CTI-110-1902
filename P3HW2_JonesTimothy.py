# Timothy Jones
# 7/15/2025
# P3HW2
# "Employee Pay Calculator" This program calculates an employee’s regular, overtime, and gross pay based on hours worked and pay rate.

#Begin
# User input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Overtime and pay calculations
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    reg_hours = 40
else:
    overtime_hours = 0
    reg_hours = hours_worked

overtime_pay = overtime_hours * (pay_rate * 1.5)
regular_pay = reg_hours * pay_rate
gross_pay = regular_pay + overtime_pay

# Print results
print("\n" + "-" * 50)
print(f"Employee name:    {employee_name}")
print()
print(f"{'Hours Worked':<15s}{'Pay Rate':<10s}{'OverTime':<10s}{'OverTime Pay':<15s}{'RegHour Pay':<15s}{'Gross Pay':<10s}")
print("-" * 90)
print(f"{hours_worked:<15.1f}{pay_rate:<10.1f}{overtime_hours:<10.1f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:.2f}")

#End
