import calendar
year=int(input("Enter the year:"))
leap_year=calendar.isleap(year)
if leap_year:
    print(year,"is leap year.")
else:
    print(year,"is not a leap year.")