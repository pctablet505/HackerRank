import calendar

month, date, year = map(int, input().split())
day = calendar.weekday(year, month, date)
print(calendar.day_name[day].upper())
