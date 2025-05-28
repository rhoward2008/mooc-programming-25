# Write your solution here
visits = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

weekly = visits * price + groceries
daily = weekly / 7

print(f'Average food expenditure:\nDaily: {daily} euros\nWeekly: {weekly} euros')