import calendar

d, m, y = map(int, input().split())

day_index = calendar.weekday(y, m, d)

print(calendar.day_name[day_index].upper())
