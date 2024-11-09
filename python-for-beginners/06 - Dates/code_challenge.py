# print today's date
from datetime import datetime, timedelta

# print yesterday's date
today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
print(yesterday)

# ask a user to enter a date
date = input('Enter a date in the format dd/mm/yyyy: ')

user_date = datetime.strptime(date, '%d/%m/%Y')

# print the date one week from the date entered
one_week = timedelta(weeks=1)
week_before = user_date - one_week
print (week_before)