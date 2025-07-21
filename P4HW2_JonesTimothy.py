# Timothy Jones
# 7/16/2025
# P4HW2
# "Employee Pay Calculator"-The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime,
# total amount paid for regular pay and total amount paid for all employees.

#Begin
# Initialize totals
employee_count = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Prompt for employee name
employee_name = input('Enter employee\'s name or "Done" to terminate: ')

while employee_name.lower() != "done":
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    # Calculate overtime
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate * 1.5)
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0.0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    # Display employee summary
    print()
    print(f"Employee name:  {employee_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<10}{'OverTime':<10}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay'}")
    print("-" * 75)
    print(f"{hours_worked:<15.1f}{pay_rate:<10.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:.2f}")
    print()

    # Update totals
    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Ask for next employee
    employee_name = input('Enter employee\'s name or "Done" to terminate: ')

# Final summary
print()
print(f"Total number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

#End
