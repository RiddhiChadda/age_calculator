import datetime

today = datetime.datetime.now()

current_year = today.year
current_month = today.month
current_day = today.day

year_born = int(input("What year were you born in? "))
month_born = int(input("What month were you born in? "))
date_born = int(input("What day were you born on? "))

age = current_year - year_born

if current_month < month_born:
    age = age - 1

elif current_month == month_born:
    if current_day < date_born:
        age = age - 1

print("Your age is:", age)