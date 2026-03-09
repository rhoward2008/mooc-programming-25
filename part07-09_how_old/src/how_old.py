from datetime import datetime

def age_diff():
    day = int(input('Day: '))
    month = int(input('Month: '))
    year = int(input('Year: '))

    date_born = datetime(year, month, day)
    y2k_date = datetime(1999,12,31)
    diff = y2k_date - date_born

    if date_born > y2k_date:
        print("You weren't born yet on the eve of the new millenium")
    elif date_born == y2k_date:
        print('You are a y2k baby!')
    else:
        print(f'You were {diff.days} days old on the eve of the new millenium')

if __name__ == '__main__':
    age_diff()