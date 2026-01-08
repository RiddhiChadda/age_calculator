import datetime
import calendar

today = datetime.datetime.now()

current_year = today.year
current_month = today.month
current_day = today.day

valid_date = False

while valid_date == False:
    year_born = int(input("What year were you born in? "))
    month_born = int(input("What month were you born in? "))
    date_born = int(input("What day were you born on? "))

    try:
        birthday = datetime.datetime(year_born, month_born, date_born)

        if birthday > today:
            print("Birth date cannot be in the future.")
            valid_date = False
        else:
            valid_date = True

    except ValueError:
        print("Invalid date. Please try again.")
        valid_date = False

age_year = current_year - birthday.year
age_month = current_month - birthday.month
age_day = current_day - birthday.day

if age_day < 0:

    if current_month == 1:
        previous_month = 12
        previous_month_year = current_year - 1
    else:
        previous_month = current_month - 1
        previous_month_year = current_year

    days_in_previous_month = calendar.monthrange(previous_month_year,previous_month)[1]

    age_month -= 1
    age_day += days_in_previous_month

if age_month < 0:
    age_year -= 1
    age_month += 12

print(
    "Your age is:", age_year, "years", age_month, "months", age_day,"days")