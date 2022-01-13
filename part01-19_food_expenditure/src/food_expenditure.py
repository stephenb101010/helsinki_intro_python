# Write your solution here
visits_weekly = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_spending = float(input("How much money do you spend on groceries in a week? "))
weekly = (visits_weekly * lunch_price) + grocery_spending
daily = weekly / 7
print("")
print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")