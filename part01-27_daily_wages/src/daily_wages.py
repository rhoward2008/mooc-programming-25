# Write your solution here
wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")

if day == "Sunday":
    daily_wages = wage * hours * 2
else:
    daily_wages = wage * hours

print(f'Daily wages: {daily_wages} euros')