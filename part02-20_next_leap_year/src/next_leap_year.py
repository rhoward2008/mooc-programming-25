# Write your solution here

def leap_year(year: int) -> bool:
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Year:"))

next_year = year + 1

while not leap_year(next_year):
    next_year += 1

print(f'The next leap year after {year} is {next_year}')