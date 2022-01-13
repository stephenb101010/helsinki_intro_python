# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day = input("Day of the week: ")
if day == "Sunday":
    hourly_wage = hourly_wage * 2
print(f"Daily wages: {hourly_wage * hours_worked} euros")