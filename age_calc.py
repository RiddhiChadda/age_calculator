import datetime

today = datetime.datetime.now()

current_year = today.year
current_month = today.month
current_day = today.day

year_born = int(input("What year were you born in? "))
month_born = int(input("What month were you born in? "))
date_born = int(input("What day were you born on? "))

age_year = current_year - year_born
age_month = current_month - month_born
age_day = current_day - date_born

if age_day < 0:
    age_month -= 1
    age_day += 30

if age_month < 0:
    age_year -= 1
    age_month += 12

print("Your age is:", age_year , "years", age_month, "months", age_day, "days")